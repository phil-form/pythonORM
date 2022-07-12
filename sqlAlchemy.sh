export FLASK_APP=app

while getopts 'm:iu' flag
do
  case "${flag}" in
    m) DB_CMD="flask db migrate -m ${OPTARG}";;
    i) DB_CMD="flask db init";;
    u) DB_CMD="flask db upgrade";;
  esac
done

if [ -z ${DB_CMD+x} ];
then
  echo -e '\nSqlAlchemy Script help :'
  echo -e '-m \t create new migration with name'
  echo -e '-u \t execute migration'
  echo -e '-i \t init project database'
else
  $DB_CMD
fi