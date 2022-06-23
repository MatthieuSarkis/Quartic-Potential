# RUN IN PARALLEL ON MULTIPLE CPUS

#parallel --bar python src/engine/main.py \
#    --atom1 {1} \
#    --atom2 {1} \
#    --r 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 \
#    --tau 0.0 0.1 0.2 \
#    --energy_unit hartree \
#    ::: H Li K Rb Cs He Ne Ar Kr Xe

parallel --bar python src/engine/main.py \
    --atom1 {1} \
    --atom2 {1} \
    --r 1.0 5.0 10.0 50.0 100.0 \
    --tau 0.0 \
    --energy_unit hartree \
    ::: H