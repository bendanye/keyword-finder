SCRIPT_DIR=$( dirname -- "$0"; )

cd $SCRIPT_DIR

source .venv/bin/activate

python3 main.py $1 $2 $3
