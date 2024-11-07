import unittest
from scientific_calculator import sin ,cos,tan,log,sqrt,exp

class TestScientificCalculator(unittest.TestCase):
         
         def test_sin_positive(self):
             self.assertAlmostEqual(sin(90), 1.0, places=1)
         
         def test_sin_negative(self):
             self.assertAlmostEqual(sin(-90), -1.0, places=1)
     
         def test_sin_zero(self):
             self.assertEqual(sin(0), 0)
 
         def test_sin_non_numeric(self):
             with self.assertRaises(TypeError):
                 sin("text")

         def test_cos_positive(self):
              self.assertAlmostEqual(cos(0), 1.0, places=1)          
              self.assertAlmostEqual(cos(180), -1.0, places=1)       
    
         def test_cos_non_numeric(self):
             with self.assertRaises(TypeError):
                 cos("text")
    

         def test_tan_positive(self):
              self.assertAlmostEqual(tan(45), 1.0, places=1)        
         def test_tan_zero(self):
              self.assertEqual(tan(0), 0)                            
    
         def test_tan_non_numeric(self):
             with self.assertRaises(TypeError):
              tan("text")
    
  
         def test_log_positive(self):
               self.assertAlmostEqual(log(1), 0, places=5)            
    
         def test_log_invalid(self):
             with self.assertRaises(ValueError):
              log(-1)                                           
    
         def test_log_non_numeric(self):
              with self.assertRaises(TypeError):
               log("text")
    
    
         def test_sqrt_positive(self):
              self.assertAlmostEqual(sqrt(4), 2, places=5)           
    
         def test_sqrt_invalid(self):
              with self.assertRaises(ValueError):
               sqrt(-1)    

         def test_sqrt_non_numeric(self):
              with self.assertRaises(TypeError):
               sqrt("text")
    
   
         def test_exp_positive(self):
            self.assertAlmostEqual(exp(1), 2.71828, places=5)      
         def test_exp_zero(self):
             self.assertEqual(exp(0), 1)                            
    
         def test_exp_non_numeric(self):
            with self.assertRaises(TypeError):
             exp("text")

if __name__ == '__main__':
    unittest.main()                 
