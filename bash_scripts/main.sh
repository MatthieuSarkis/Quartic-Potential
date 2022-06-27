# RUN IN PARALLEL ON MULTIPLE CPUS

parallel --bar python src/engine/main.py \
    --atom1 {1} \
    --atom2 {1} \
    --r 0.5 1.0 1.5 2.0 2.5 3.0 \
    --tau 0.0 \
    --energy_unit hartree \
    ::: H Li K Rb Cs He Ne Ar Kr Xe

#parallel --bar python src/engine/main.py \
#    --atom1 {1} \
#    --atom2 {1} \
#    --r 0.5 1.0 1.5 2.0 2.5 3.0 \
#    --tau 0.0 \
#    --energy_unit hartree \
#    ::: H