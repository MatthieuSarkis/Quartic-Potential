# RUN SEQUENTIALLY

#for ATOM in H Li K Rb Cs He Ne Ar Kr Xe
#do
#    python src/engine/main.py \
#        --atom1 $ATOM \
#        --atom2 $ATOM \
#        --r 1.0 2.0 5.0 10.0 20.0 \
#        --tau 0.0 1.0 2.0 5.0 10.0, 20.0 \
#        --energy_unit hartree
#done

# RUN IN PARALLEL ON MULTIPLE CPUS

#parallel --jobs 10 --bar python src/engine/main.py \
#    --atom1 {1} \
#    --atom2 {1} \
#    --r 1.0 2.0 5.0 10.0 20.0 \
#    --tau 0.0 1.0 2.0 5.0 10.0, 20.0 \
#    --energy_unit hartree \
#    ::: H Li K Rb Cs He Ne Ar Kr Xe

parallel --bar python src/engine/main.py \
    --atom1 {1} \
    --atom2 {1} \
    --r 1.0 2.0 5.0 7.0 10.0 15.0 20.0 \
    --tau 0.0 5.0 10.0 \
    --energy_unit hartree \
    ::: H Li K Rb Cs He Ne Ar Kr Xe