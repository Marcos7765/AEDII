SEEDS="Pretzel Caipirinha Chahan_(dish)"

#uncomment line 5 and you'll have a script to run it over any ammount of seeds
#that you want. Use "_" instead of space for seeds with multiple words
#SEEDS=$@

format() {
    python -c "print(\"$@\".replace(\"_\", \" \"))"
}

for SEED in $SEEDS; do
    echo Running makeGraph.py on $SEED
    python makeGraph.py `format $SEED`
    python -c 'print(80*"-")'
done

python joinAndFilter.py unfiltered_*