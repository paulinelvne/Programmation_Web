#!/bin/sh
#set -x

ROOT=$(dirname "$(readlink -f $0)")
SCRIPT=$(basename $0)
VENV="${ROOT}/.venv"
PYTHON3="${VENV}/bin/python3"
PIP="${VENV}/bin/pip"

#export APP_SETTINGS=${APP_SETTINGS:-config.Development}

_inspect () {
  # Auto generate help string
  local help=$(awk '$1 ~ /^[a-z]+_?[a-z]+$/ && $2 == "()" { printf "%s|", $1 }' $0)
  echo ${help%|}
}

_is_exe () {
  command -v $1 >/dev/null 2>&1 || \
    { echo >&2 "missing $1 command"; return 1; }; return 0
  }
#-----------------------------------------------------------------------------#

_mkvenv () {
  local red=$(tput setaf 1)
  local green=$(tput setaf 2)
  local yellow=$(tput setaf 3)
  local r=$(tput sgr0)
  printf "Setting up python virtualenv in:\n“${VENV}”\n"
  _is_exe python3 || exit 1
  python3 -m venv "${VENV}" || { echo "${red}Error seting up venv${r}"; exit 1; }
  printf "${green}→ installing:${r} ${yellow}wheel${r}…"
  "${PIP}" --quiet install wheel || { echo "${red}Error installing wheel${r}"; exit 1; }
  printf " ${yellow} requirements…${r}"
  "${PIP}" --quiet install --requirement ${ROOT}/requirement.txt || { echo "${red}Error setting up venv${r}"; exit 1; }
  printf " ${green}done!${r}\n"
}


serve () {
  #FLASK_APP=app ${VENV}/bin/flask run
  "${PYTHON3}" "${ROOT}/app.py"
}

shell () {
  FLASK_APP=app "${VENV}/bin/flask" shell -i -c "from model import User, Field, db"
}

# virtualenv generation
if [ ! -e "${VENV}/bin/activate" ];then
    _mkvenv
fi

if [ $# -eq 0 ]
then
  echo "./${SCRIPT} $(_inspect)"
  exit
fi


$@

# vim: fileencoding=utf8 ft=sh
