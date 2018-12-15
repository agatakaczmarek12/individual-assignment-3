# -*- coding: utf-8 -*-

#%% Exercise 1

from exercises import recalculate_quality, ham

def test_lessthan5_recalculation():
 
    recalculate_quality(ham)
    assert ham.quality == 1
    
#%% Excercise 1
    
from exercises import recalculate_quality, carrot    
    
def test_zero_quality_product():
    
    recalculate_quality(carrot)
    assert carrot.quality == 0
    
#%% Excersise 1
    
from exercises import recalculate_quality, potatoe  
    
def test_defined_product():
    
    recalculate_quality(potatoe)
    assert potatoe.quality == 9.5
