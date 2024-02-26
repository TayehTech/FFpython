from . import AVOptions
from .filter_class import Filter
from dataclasses import dataclass

@dataclass(repr=False, eq=False)
class abench(Filter, AVOptions.abench, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ABENCH ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class acompressor(Filter, AVOptions.acompressor_sidechaincompress, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ ACOMPRESSOR ┣━━━━━╸'default'      
-          audio        ┃             ┃        audio        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class acontrast(Filter, AVOptions.acontrast, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ ACONTRAST ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class acopy(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ ACOPY ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class acue(Filter, AVOptions._a_cue, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ ACUE ┣━━━━━╸'default'          
-             audio        ┃      ┃        audio            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class acrossfade(Filter, AVOptions.acrossfade, inputs_count=2, outputs_count=1):
    """
-                                                           
-      'crossfade0'╺━┓   ┏━━━━━━━━━━━━┓                     
-         audio      ┗━━━┫            ┃                     
-                        ┃            ┃                     
-                        ┃ ACROSSFADE ┣━━━━━╸'default'      
-                        ┃            ┃        audio        
-                    ┏━━━┫            ┃                     
-      'crossfade1'╺━┛   ┗━━━━━━━━━━━━┛                     
-         audio                                             
"""
@dataclass(repr=False, eq=False)
class acrossover(Filter, AVOptions.acrossover, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ ACROSSOVER ┣━━━━━╸'dynamic'       
-          audio        ┃            ┃                      
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class acrusher(Filter, AVOptions.acrusher, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ ACRUSHER ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class adeclick(Filter, AVOptions.adeclick, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ ADECLICK ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class adeclip(Filter, AVOptions.adeclip, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ ADECLIP ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class adecorrelate(Filter, AVOptions.adecorrelate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ ADECORRELATE ┣━━━━━╸'default'      
-         audio        ┃              ┃        audio        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class adelay(Filter, AVOptions.adelay, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ADELAY ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class adenorm(Filter, AVOptions.adenorm, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ ADENORM ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class aderivative(Filter, AVOptions.aderivative_aintegral, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ ADERIVATIVE ┣━━━━━╸'default'      
-          audio        ┃             ┃        audio        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class adrc(Filter, AVOptions.adrc, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ ADRC ┣━━━━━╸'default'          
-             audio        ┃      ┃        audio            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class adynamicequalizer(Filter, AVOptions.adynamicequalizer, inputs_count=1, outputs_count=1):
    """
-                                                           
-                    ┏━━━━━━━━━━━━━━━━━━━┓                  
-                    ┃                   ┃                  
-     'default'╺━━━━━┫ ADYNAMICEQUALIZER ┣━━━━━╸'default'   
-       audio        ┃                   ┃        audio     
-                    ┗━━━━━━━━━━━━━━━━━━━┛                  
-                                                           
"""
@dataclass(repr=False, eq=False)
class adynamicsmooth(Filter, AVOptions.adynamicsmooth, inputs_count=1, outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━━━┓                    
-                     ┃                ┃                    
-      'default'╺━━━━━┫ ADYNAMICSMOOTH ┣━━━━━╸'default'     
-        audio        ┃                ┃        audio       
-                     ┗━━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class aecho(Filter, AVOptions.aecho, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ AECHO ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class aemphasis(Filter, AVOptions.aemphasis, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ AEMPHASIS ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class aeval(Filter, AVOptions.aeval, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ AEVAL ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class aexciter(Filter, AVOptions.aexciter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ AEXCITER ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class afade(Filter, AVOptions.afade, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ AFADE ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class afftdn(Filter, AVOptions.afftdn, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ AFFTDN ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class afftfilt(Filter, AVOptions.afftfilt, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ AFFTFILT ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class afir(Filter, AVOptions.afir, inputs_count="dynamic", outputs_count="dynamic"):
    """
-                                                           
-                         ┏━━━━━━┓                          
-                         ┃      ┃                          
-          'dynamic'╺━━━━━┫ AFIR ┣━━━━━╸'dynamic'           
-                         ┃      ┃                          
-                         ┗━━━━━━┛                          
-                                                           
"""
@dataclass(repr=False, eq=False)
class aformat(Filter, AVOptions.aformat, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ AFORMAT ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class afreqshift(Filter, AVOptions.afreqshift, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ AFREQSHIFT ┣━━━━━╸'default'       
-          audio        ┃            ┃        audio         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class afwtdn(Filter, AVOptions.afwtdn, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ AFWTDN ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class agate(Filter, AVOptions.agate_sidechaingate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ AGATE ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class aiir(Filter, AVOptions.aiir, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ AIIR ┣━━━━━╸'dynamic'          
-             audio        ┃      ┃                         
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class aintegral(Filter, AVOptions.aderivative_aintegral, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ AINTEGRAL ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class ainterleave(Filter, AVOptions.ainterleave, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━┓                       
-                     ┃             ┃                       
-      'dynamic'╺━━━━━┫ AINTERLEAVE ┣━━━━━╸'default'        
-                     ┃             ┃        audio          
-                     ┗━━━━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class alatency(Filter, inputs_count=1, outputs_count=2):
    """
-                                                           
-     ╺━━━━┓  ┏━━╸'default'                                 
-          ┣━━┛     audio                                   
-          ┃                                                
-     ENCY ┃                                                
-          ┃                                                
-          ┣━━┓                                             
-     ╺━━━━┛  ┗━━╸'This'                                    
-     ort for timeline through the 'enable' option.         
"""
@dataclass(repr=False, eq=False)
class alimiter(Filter, AVOptions.alimiter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━┓                        
-                       ┃          ┃                        
-           'main'╺━━━━━┫ ALIMITER ┣━━━━━╸'default'         
-            audio      ┃          ┃        audio           
-                       ┗━━━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class allpass(Filter, AVOptions.allpass, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ ALLPASS ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class aloop(Filter, AVOptions.aloop, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ ALOOP ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class amerge(Filter, AVOptions.amerge, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━┓                         
-                        ┃        ┃                         
-         'dynamic'╺━━━━━┫ AMERGE ┣━━━━━╸'default'          
-                        ┃        ┃        audio            
-                        ┗━━━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class ametadata(Filter, AVOptions.ametadata, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ AMETADATA ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class amix(Filter, AVOptions.amix, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━┓                          
-                         ┃      ┃                          
-          'dynamic'╺━━━━━┫ AMIX ┣━━━━━╸'default'           
-                         ┃      ┃        audio             
-                         ┗━━━━━━┛                          
-                                                           
"""
@dataclass(repr=False, eq=False)
class amultiply(Filter, inputs_count=2, outputs_count=1):
    """
-                                                           
-       'multiply0'╺━┓   ┏━━━━━━━━━━━┓                      
-          audio     ┗━━━┫           ┃                      
-                        ┃           ┃                      
-                        ┃ AMULTIPLY ┣━━━━━╸'default'       
-                        ┃           ┃        audio         
-                    ┏━━━┫           ┃                      
-       'multiply1'╺━┛   ┗━━━━━━━━━━━┛                      
-          audio                                            
"""
@dataclass(repr=False, eq=False)
class anequalizer(Filter, AVOptions.anequalizer, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ ANEQUALIZER ┣━━━━━╸'dynamic'      
-          audio        ┃             ┃                     
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class anlmdn(Filter, AVOptions.anlmdn, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ANLMDN ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class anlmf(Filter, AVOptions.anlm_f_s_, inputs_count=2, outputs_count=1):
    """
-                                                           
-             'input'╺━┓   ┏━━━━━━━┓                        
-              audio   ┗━━━┫       ┃                        
-                          ┃       ┃                        
-                          ┃ ANLMF ┣━━━━━╸'default'         
-                          ┃       ┃        audio           
-                      ┏━━━┫       ┃                        
-           'desired'╺━┛   ┗━━━━━━━┛                        
-             audio                                         
"""
@dataclass(repr=False, eq=False)
class anlms(Filter, AVOptions.anlm_f_s_, inputs_count=2, outputs_count=1):
    """
-                                                           
-             'input'╺━┓   ┏━━━━━━━┓                        
-              audio   ┗━━━┫       ┃                        
-                          ┃       ┃                        
-                          ┃ ANLMS ┣━━━━━╸'default'         
-                          ┃       ┃        audio           
-                      ┏━━━┫       ┃                        
-           'desired'╺━┛   ┗━━━━━━━┛                        
-             audio                                         
"""
@dataclass(repr=False, eq=False)
class anull(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ ANULL ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class apad(Filter, AVOptions.apad, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ APAD ┣━━━━━╸'default'          
-             audio        ┃      ┃        audio            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class aperms(Filter, AVOptions._a_perms, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ APERMS ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class aphaser(Filter, AVOptions.aphaser, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ APHASER ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class aphaseshift(Filter, AVOptions.aphaseshift, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ APHASESHIFT ┣━━━━━╸'default'      
-          audio        ┃             ┃        audio        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class apsyclip(Filter, AVOptions.apsyclip, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ APSYCLIP ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class apulsator(Filter, AVOptions.apulsator, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ APULSATOR ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class arealtime(Filter, AVOptions._a_realtime, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ AREALTIME ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class aresample(Filter, AVOptions.SWResampler, AVOptions.aresample, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ ARESAMPLE ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class areverse(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ AREVERSE ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class arnndn(Filter, AVOptions.arnndn, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ARNNDN ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class asdr(Filter, inputs_count=2, outputs_count=1):
    """
-                                                           
-            'input0'╺━┓   ┏━━━━━━┓                         
-             audio    ┗━━━┫      ┃                         
-                          ┃      ┃                         
-                          ┃ ASDR ┣━━━━━╸'default'          
-                          ┃      ┃        audio            
-                      ┏━━━┫      ┃                         
-            'input1'╺━┛   ┗━━━━━━┛                         
-             audio                                         
"""
@dataclass(repr=False, eq=False)
class asegment(Filter, AVOptions.asegment, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ ASEGMENT ┣━━━━━╸'dynamic'        
-           audio        ┃          ┃                       
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class aselect(Filter, AVOptions.aselect, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ ASELECT ┣━━━━━╸'dynamic'        
-            audio        ┃         ┃                       
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class asendcmd(Filter, AVOptions._a_sendcmd, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ ASENDCMD ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class asetnsamples(Filter, AVOptions.asetnsamples, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ ASETNSAMPLES ┣━━━━━╸'default'      
-         audio        ┃              ┃        audio        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class asetpts(Filter, AVOptions.asetpts, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ ASETPTS ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class asetrate(Filter, AVOptions.asetrate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ ASETRATE ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class asettb(Filter, AVOptions.asettb, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ASETTB ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class ashowinfo(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ ASHOWINFO ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class asidedata(Filter, AVOptions.asidedata, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ ASIDEDATA ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class asoftclip(Filter, AVOptions.asoftclip, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ ASOFTCLIP ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class aspectralstats(Filter, AVOptions.aspectralstats, inputs_count=1, outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━━━┓                    
-                     ┃                ┃                    
-      'default'╺━━━━━┫ ASPECTRALSTATS ┣━━━━━╸'default'     
-        audio        ┃                ┃        audio       
-                     ┗━━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class asplit(Filter, AVOptions._a_split, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ASPLIT ┣━━━━━╸'dynamic'         
-            audio        ┃        ┃                        
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class astats(Filter, AVOptions.astats, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ASTATS ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class astreamselect(Filter, AVOptions._a_streamselect, inputs_count="dynamic", outputs_count="dynamic"):
    """
-                                                           
-                    ┏━━━━━━━━━━━━━━━┓                      
-                    ┃               ┃                      
-     'dynamic'╺━━━━━┫ ASTREAMSELECT ┣━━━━━╸'dynamic'       
-                    ┃               ┃                      
-                    ┗━━━━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class asubboost(Filter, AVOptions.asubboost, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ ASUBBOOST ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class asubcut(Filter, AVOptions.asubcut, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ ASUBCUT ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class asupercut(Filter, AVOptions.asupercut, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ ASUPERCUT ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class asuperpass(Filter, AVOptions.asuperpass_asuperstop, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ ASUPERPASS ┣━━━━━╸'default'       
-          audio        ┃            ┃        audio         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class asuperstop(Filter, AVOptions.asuperpass_asuperstop, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ ASUPERSTOP ┣━━━━━╸'default'       
-          audio        ┃            ┃        audio         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class atempo(Filter, AVOptions.atempo, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ATEMPO ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class atilt(Filter, AVOptions.atilt, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ ATILT ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class atrim(Filter, AVOptions.atrim, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ ATRIM ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class axcorrelate(Filter, AVOptions.axcorrelate, inputs_count=2, outputs_count=1):
    """
-                                                           
-     'axcorrelate0╺━┓   ┏━━━━━━━━━━━━━┓                    
-        audio       ┗━━━┫             ┃                    
-                        ┃             ┃                    
-                        ┃ AXCORRELATE ┣━━━━━╸'default'     
-                        ┃             ┃        audio       
-                    ┏━━━┫             ┃                    
-     'axcorrelate1╺━┛   ┗━━━━━━━━━━━━━┛                    
-        audio                                              
"""
@dataclass(repr=False, eq=False)
class azmq(Filter, AVOptions._a_zmq, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ AZMQ ┣━━━━━╸'default'          
-             audio        ┃      ┃        audio            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class bandpass(Filter, AVOptions.bandpass, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ BANDPASS ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class bandreject(Filter, AVOptions.bandreject, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ BANDREJECT ┣━━━━━╸'default'       
-          audio        ┃            ┃        audio         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class bass(Filter, AVOptions.bass_lowshelf, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ BASS ┣━━━━━╸'default'          
-             audio        ┃      ┃        audio            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class biquad(Filter, AVOptions.biquad, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ BIQUAD ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class channelmap(Filter, AVOptions.channelmap, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ CHANNELMAP ┣━━━━━╸'default'       
-          audio        ┃            ┃        audio         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class channelsplit(Filter, AVOptions.channelsplit, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ CHANNELSPLIT ┣━━━━━╸'dynamic'      
-         audio        ┃              ┃                     
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class chorus(Filter, AVOptions.chorus, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ CHORUS ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class compand(Filter, AVOptions.compand, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ COMPAND ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class compensationdelay(Filter, AVOptions.compensationdelay, inputs_count=1, outputs_count=1):
    """
-                                                           
-                    ┏━━━━━━━━━━━━━━━━━━━┓                  
-                    ┃                   ┃                  
-     'default'╺━━━━━┫ COMPENSATIONDELAY ┣━━━━━╸'default'   
-       audio        ┃                   ┃        audio     
-                    ┗━━━━━━━━━━━━━━━━━━━┛                  
-                                                           
"""
@dataclass(repr=False, eq=False)
class crossfeed(Filter, AVOptions.crossfeed, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ CROSSFEED ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class crystalizer(Filter, AVOptions.crystalizer, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ CRYSTALIZER ┣━━━━━╸'default'      
-          audio        ┃             ┃        audio        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class dcshift(Filter, AVOptions.dcshift, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ DCSHIFT ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class deesser(Filter, AVOptions.deesser, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ DEESSER ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class dialoguenhance(Filter, AVOptions.dialoguenhance, inputs_count=1, outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━━━┓                    
-                     ┃                ┃                    
-      'default'╺━━━━━┫ DIALOGUENHANCE ┣━━━━━╸'default'     
-        audio        ┃                ┃        audio       
-                     ┗━━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class drmeter(Filter, AVOptions.drmeter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ DRMETER ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class dynaudnorm(Filter, AVOptions.dynaudnorm, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ DYNAUDNORM ┣━━━━━╸'default'       
-          audio        ┃            ┃        audio         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class earwax(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ EARWAX ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class ebur128(Filter, AVOptions.ebur128, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ EBUR128 ┣━━━━━╸'dynamic'        
-            audio        ┃         ┃                       
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class equalizer(Filter, AVOptions.equalizer, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ EQUALIZER ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class extrastereo(Filter, AVOptions.extrastereo, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ EXTRASTEREO ┣━━━━━╸'default'      
-          audio        ┃             ┃        audio        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class firequalizer(Filter, AVOptions.firequalizer, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ FIREQUALIZER ┣━━━━━╸'default'      
-         audio        ┃              ┃        audio        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class flanger(Filter, AVOptions.flanger, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ FLANGER ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class haas(Filter, AVOptions.haas, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ HAAS ┣━━━━━╸'default'          
-             audio        ┃      ┃        audio            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class hdcd(Filter, AVOptions.hdcd, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ HDCD ┣━━━━━╸'default'          
-             audio        ┃      ┃        audio            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class headphone(Filter, AVOptions.headphone, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━┓                        
-                      ┃           ┃                        
-       'dynamic'╺━━━━━┫ HEADPHONE ┣━━━━━╸'default'         
-                      ┃           ┃        audio           
-                      ┗━━━━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class highpass(Filter, AVOptions.highpass, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ HIGHPASS ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class highshelf(Filter, AVOptions.treble_high_tiltshelf, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ HIGHSHELF ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class join(Filter, AVOptions.join, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━┓                          
-                         ┃      ┃                          
-          'dynamic'╺━━━━━┫ JOIN ┣━━━━━╸'default'           
-                         ┃      ┃        audio             
-                         ┗━━━━━━┛                          
-                                                           
"""
@dataclass(repr=False, eq=False)
class loudnorm(Filter, AVOptions.loudnorm, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ LOUDNORM ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class lowpass(Filter, AVOptions.lowpass, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ LOWPASS ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class lowshelf(Filter, AVOptions.bass_lowshelf, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ LOWSHELF ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class mcompand(Filter, AVOptions.mcompand, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ MCOMPAND ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class pan(Filter, AVOptions.pan, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ PAN ┣━━━━━╸'default'          
-              audio        ┃     ┃        audio            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class replaygain(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ REPLAYGAIN ┣━━━━━╸'default'       
-          audio        ┃            ┃        audio         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class rubberband(Filter, AVOptions.rubberband, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ RUBBERBAND ┣━━━━━╸'default'       
-          audio        ┃            ┃        audio         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class sidechaincompress(Filter, AVOptions.acompressor_sidechaincompress, inputs_count=2, outputs_count=1):
    """
-                                                           
-        'main'╺━┓   ┏━━━━━━━━━━━━━━━━━━━┓                  
-         audio  ┗━━━┫                   ┃                  
-                    ┃                   ┃                  
-                    ┃ SIDECHAINCOMPRESS ┣━━━━━╸'default'   
-                    ┃                   ┃        audio     
-                ┏━━━┫                   ┃                  
-     sidechain╺━┛   ┗━━━━━━━━━━━━━━━━━━━┛                  
-      audio                                                
"""
@dataclass(repr=False, eq=False)
class sidechaingate(Filter, AVOptions.agate_sidechaingate, inputs_count=2, outputs_count=1):
    """
-                                                           
-          'main'╺━┓   ┏━━━━━━━━━━━━━━━┓                    
-           audio  ┗━━━┫               ┃                    
-                      ┃               ┃                    
-                      ┃ SIDECHAINGATE ┣━━━━━╸'default'     
-                      ┃               ┃        audio       
-                  ┏━━━┫               ┃                    
-     'sidechain'╺━┛   ┗━━━━━━━━━━━━━━━┛                    
-        audio                                              
"""
@dataclass(repr=False, eq=False)
class silencedetect(Filter, AVOptions.silencedetect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ SILENCEDETECT ┣━━━━━╸'default'     
-         audio        ┃               ┃        audio       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class silenceremove(Filter, AVOptions.silenceremove, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ SILENCEREMOVE ┣━━━━━╸'default'     
-         audio        ┃               ┃        audio       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class speechnorm(Filter, AVOptions.speechnorm, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ SPEECHNORM ┣━━━━━╸'default'       
-          audio        ┃            ┃        audio         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class stereotools(Filter, AVOptions.stereotools, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ STEREOTOOLS ┣━━━━━╸'default'      
-          audio        ┃             ┃        audio        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class stereowiden(Filter, AVOptions.stereowiden, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ STEREOWIDEN ┣━━━━━╸'default'      
-          audio        ┃             ┃        audio        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class superequalizer(Filter, AVOptions.superequalizer, inputs_count=1, outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━━━┓                    
-                     ┃                ┃                    
-      'default'╺━━━━━┫ SUPEREQUALIZER ┣━━━━━╸'default'     
-        audio        ┃                ┃        audio       
-                     ┗━━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class surround(Filter, AVOptions.surround, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ SURROUND ┣━━━━━╸'default'        
-           audio        ┃          ┃        audio          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class tiltshelf(Filter, AVOptions.treble_high_tiltshelf, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ TILTSHELF ┣━━━━━╸'default'       
-           audio        ┃           ┃        audio         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class treble(Filter, AVOptions.treble_high_tiltshelf, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ TREBLE ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class tremolo(Filter, AVOptions.tremolo, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ TREMOLO ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class vibrato(Filter, AVOptions.vibrato, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ VIBRATO ┣━━━━━╸'default'        
-            audio        ┃         ┃        audio          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class virtualbass(Filter, AVOptions.virtualbass, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ VIRTUALBASS ┣━━━━━╸'default'      
-          audio        ┃             ┃        audio        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class volume(Filter, AVOptions.volume, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ VOLUME ┣━━━━━╸'default'         
-            audio        ┃        ┃        audio           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class volumedetect(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ VOLUMEDETECT ┣━━━━━╸'default'      
-         audio        ┃              ┃        audio        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class aevalsrc(Filter, AVOptions.aevalsrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━━┓                      
-                         ┃          ┃                      
-             'none'╺━━━━━┫ AEVALSRC ┣━━━━━╸'default'       
-          source filter  ┃          ┃        audio         
-                         ┗━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class afdelaysrc(Filter, AVOptions.afdelaysrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━┓                     
-                        ┃            ┃                     
-            'none'╺━━━━━┫ AFDELAYSRC ┣━━━━━╸'default'      
-         source filter  ┃            ┃        audio        
-                        ┗━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class afirsrc(Filter, AVOptions.afirsrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━━━┓                      
-                          ┃         ┃                      
-              'none'╺━━━━━┫ AFIRSRC ┣━━━━━╸'default'       
-          source filter   ┃         ┃        audio         
-                          ┗━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class anoisesrc(Filter, AVOptions.anoisesrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━━━┓                     
-                         ┃           ┃                     
-             'none'╺━━━━━┫ ANOISESRC ┣━━━━━╸'default'      
-         source filter   ┃           ┃        audio        
-                         ┗━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class anullsrc(Filter, AVOptions.anullsrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━━┓                      
-                         ┃          ┃                      
-             'none'╺━━━━━┫ ANULLSRC ┣━━━━━╸'default'       
-          source filter  ┃          ┃        audio         
-                         ┗━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class hilbert(Filter, AVOptions.hilbert, inputs_count=0, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━━━┓                      
-                          ┃         ┃                      
-              'none'╺━━━━━┫ HILBERT ┣━━━━━╸'default'       
-          source filter   ┃         ┃        audio         
-                          ┗━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class sinc(Filter, AVOptions.sinc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━━┓                        
-                           ┃      ┃                        
-               'none'╺━━━━━┫ SINC ┣━━━━━╸'default'         
-            source filter  ┃      ┃        audio           
-                           ┗━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class sine(Filter, AVOptions.sine, inputs_count=0, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━━┓                        
-                           ┃      ┃                        
-               'none'╺━━━━━┫ SINE ┣━━━━━╸'default'         
-            source filter  ┃      ┃        audio           
-                           ┗━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class anullsink(Filter, inputs_count=1, outputs_count=0):
    """
-                                                           
-                       ┏━━━━━━━━━━━┓                       
-                       ┃           ┃                       
-        'default'╺━━━━━┫ ANULLSINK ┣━━━━━╸'none'           
-          audio        ┃           ┃   sink filter         
-                       ┗━━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class addroi(Filter, AVOptions.addroi, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ADDROI ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class alphaextract(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ ALPHAEXTRACT ┣━━━━━╸'default'      
-         video        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class alphamerge(Filter, AVOptions.framesync, AVOptions.alphamerge, inputs_count=2, outputs_count=1):
    """
-                                                           
-           'main'╺━┓   ┏━━━━━━━━━━━━┓                      
-           video   ┗━━━┫            ┃                      
-                       ┃            ┃                      
-                       ┃ ALPHAMERGE ┣━━━━━╸'default'       
-                       ┃            ┃        video         
-                   ┏━━━┫            ┃                      
-          'alpha'╺━┛   ┗━━━━━━━━━━━━┛                      
-           video                                           
"""
@dataclass(repr=False, eq=False)
class amplify(Filter, AVOptions.amplify, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ AMPLIFY ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class ass(Filter, AVOptions.ass, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ ASS ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class atadenoise(Filter, AVOptions.atadenoise, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ ATADENOISE ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class avgblur(Filter, AVOptions.avgblur, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ AVGBLUR ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class backgroundkey(Filter, AVOptions.backgroundkey, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ BACKGROUNDKEY ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class bbox(Filter, AVOptions.bbox, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ BBOX ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class bench(Filter, AVOptions.bench, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ BENCH ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class bilateral(Filter, AVOptions.bilateral, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ BILATERAL ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class bitplanenoise(Filter, AVOptions.bitplanenoise, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ BITPLANENOISE ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class blackdetect(Filter, AVOptions.blackdetect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ BLACKDETECT ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class blackframe(Filter, AVOptions.blackframe, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ BLACKFRAME ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class blend(Filter, AVOptions.framesync, AVOptions.blend, inputs_count=2, outputs_count=1):
    """
-                                                           
-              'top'╺━┓   ┏━━━━━━━┓                         
-              video  ┗━━━┫       ┃                         
-                         ┃       ┃                         
-                         ┃ BLEND ┣━━━━━╸'default'          
-                         ┃       ┃        video            
-                     ┏━━━┫       ┃                         
-           'bottom'╺━┛   ┗━━━━━━━┛                         
-             video                                         
"""
@dataclass(repr=False, eq=False)
class blockdetect(Filter, AVOptions.blockdetect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ BLOCKDETECT ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class blurdetect(Filter, AVOptions.blurdetect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ BLURDETECT ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class bm3d(Filter, AVOptions.bm3d, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━┓                          
-                         ┃      ┃                          
-          'dynamic'╺━━━━━┫ BM3D ┣━━━━━╸'default'           
-                         ┃      ┃        video             
-                         ┗━━━━━━┛                          
-                                                           
"""
@dataclass(repr=False, eq=False)
class boxblur(Filter, AVOptions.boxblur, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ BOXBLUR ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class bwdif(Filter, AVOptions.bwdif, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ BWDIF ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class cas(Filter, AVOptions.cas, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ CAS ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class chromahold(Filter, AVOptions.chromahold, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ CHROMAHOLD ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class chromakey(Filter, AVOptions.chromakey, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ CHROMAKEY ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class chromanr(Filter, AVOptions.chromanr, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ CHROMANR ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class chromashift(Filter, AVOptions.chromashift, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ CHROMASHIFT ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class ciescope(Filter, AVOptions.ciescope, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ CIESCOPE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class codecview(Filter, AVOptions.codecview, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ CODECVIEW ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorbalance(Filter, AVOptions.colorbalance, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ COLORBALANCE ┣━━━━━╸'default'      
-         video        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorchannelmixer(Filter, AVOptions.colorchannelmixer, inputs_count=1, outputs_count=1):
    """
-                                                           
-                    ┏━━━━━━━━━━━━━━━━━━━┓                  
-                    ┃                   ┃                  
-     'default'╺━━━━━┫ COLORCHANNELMIXER ┣━━━━━╸'default'   
-       video        ┃                   ┃        video     
-                    ┗━━━━━━━━━━━━━━━━━━━┛                  
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorcontrast(Filter, AVOptions.colorcontrast, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ COLORCONTRAST ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorcorrect(Filter, AVOptions.colorcorrect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ COLORCORRECT ┣━━━━━╸'default'      
-         video        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorize(Filter, AVOptions.colorize, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ COLORIZE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorkey(Filter, AVOptions.colorkey, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ COLORKEY ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorhold(Filter, AVOptions.colorhold, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ COLORHOLD ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorlevels(Filter, AVOptions.colorlevels, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ COLORLEVELS ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class colormap(Filter, AVOptions.colormap, inputs_count=3, outputs_count=1):
    """
-                                                           
-         'default'╺━┓   ┏━━━━━━━━━━┓                       
-           video    ┗━━━┫          ┃                       
-                        ┃          ┃                       
-                        ┃          ┃                       
-          'source'╺━━━━━┫ COLORMAP ┣━━━━━╸'default'        
-            video       ┃          ┃        video          
-                        ┃          ┃                       
-                    ┏━━━┫          ┃                       
-          'target'╺━┛   ┗━━━━━━━━━━┛                       
-            video                                          
"""
@dataclass(repr=False, eq=False)
class colormatrix(Filter, AVOptions.colormatrix, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ COLORMATRIX ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorspace(Filter, AVOptions.colorspace, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ COLORSPACE ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class colortemperature(Filter, AVOptions.colortemperature, inputs_count=1, outputs_count=1):
    """
-                                                           
-                    ┏━━━━━━━━━━━━━━━━━━┓                   
-                    ┃                  ┃                   
-     'default'╺━━━━━┫ COLORTEMPERATURE ┣━━━━━╸'default'    
-       video        ┃                  ┃        video      
-                    ┗━━━━━━━━━━━━━━━━━━┛                   
-                                                           
"""
@dataclass(repr=False, eq=False)
class convolution(Filter, AVOptions.convolution, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ CONVOLUTION ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class convolve(Filter, AVOptions.framesync, AVOptions.convolve, inputs_count=2, outputs_count=1):
    """
-                                                           
-            'main'╺━┓   ┏━━━━━━━━━━┓                       
-             video  ┗━━━┫          ┃                       
-                        ┃          ┃                       
-                        ┃ CONVOLVE ┣━━━━━╸'default'        
-                        ┃          ┃        video          
-                    ┏━━━┫          ┃                       
-         'impulse'╺━┛   ┗━━━━━━━━━━┛                       
-           video                                           
"""
@dataclass(repr=False, eq=False)
class copy(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ COPY ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class coreimage(Filter, AVOptions.coreimage, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ COREIMAGE ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class corr(Filter, AVOptions.framesync, AVOptions.corr, inputs_count=2, outputs_count=1):
    """
-                                                           
-               'main'╺━┓   ┏━━━━━━┓                        
-               video   ┗━━━┫      ┃                        
-                           ┃      ┃                        
-                           ┃ CORR ┣━━━━━╸'default'         
-                           ┃      ┃        video           
-                       ┏━━━┫      ┃                        
-          'reference'╺━┛   ┗━━━━━━┛                        
-             video                                         
"""
@dataclass(repr=False, eq=False)
class cover_rect(Filter, AVOptions.cover_rect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ COVER_RECT ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class crop(Filter, AVOptions.crop, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ CROP ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class cropdetect(Filter, AVOptions.cropdetect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ CROPDETECT ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class cue(Filter, AVOptions._a_cue, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ CUE ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class curves(Filter, AVOptions.curves, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ CURVES ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class datascope(Filter, AVOptions.datascope, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ DATASCOPE ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class dblur(Filter, AVOptions.dblur, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ DBLUR ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class dctdnoiz(Filter, AVOptions.dctdnoiz, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ DCTDNOIZ ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class deband(Filter, AVOptions.deband, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ DEBAND ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class deblock(Filter, AVOptions.deblock, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ DEBLOCK ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class decimate(Filter, AVOptions.decimate, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━┓                        
-                       ┃          ┃                        
-        'dynamic'╺━━━━━┫ DECIMATE ┣━━━━━╸'default'         
-                       ┃          ┃        video           
-                       ┗━━━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class deconvolve(Filter, AVOptions.framesync, AVOptions.deconvolve, inputs_count=2, outputs_count=1):
    """
-                                                           
-           'main'╺━┓   ┏━━━━━━━━━━━━┓                      
-            video  ┗━━━┫            ┃                      
-                       ┃            ┃                      
-                       ┃ DECONVOLVE ┣━━━━━╸'default'       
-                       ┃            ┃        video         
-                   ┏━━━┫            ┃                      
-        'impulse'╺━┛   ┗━━━━━━━━━━━━┛                      
-          video                                            
"""
@dataclass(repr=False, eq=False)
class dedot(Filter, AVOptions.dedot, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ DEDOT ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class deflate(Filter, AVOptions.deflate_inflate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ DEFLATE ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class deflicker(Filter, AVOptions.deflicker, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ DEFLICKER ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class dejudder(Filter, AVOptions.dejudder, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ DEJUDDER ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class delogo(Filter, AVOptions.delogo, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ DELOGO ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class derain(Filter, AVOptions.derain, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ DERAIN ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class deshake(Filter, AVOptions.deshake, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ DESHAKE ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class despill(Filter, AVOptions.despill, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ DESPILL ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class detelecine(Filter, AVOptions.detelecine, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ DETELECINE ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class dilation(Filter, AVOptions.erosion_dilation, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ DILATION ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class displace(Filter, AVOptions.displace, inputs_count=3, outputs_count=1):
    """
-                                                           
-          'source'╺━┓   ┏━━━━━━━━━━┓                       
-           video    ┗━━━┫          ┃                       
-                        ┃          ┃                       
-                        ┃          ┃                       
-            'xmap'╺━━━━━┫ DISPLACE ┣━━━━━╸'default'        
-            video       ┃          ┃        video          
-                        ┃          ┃                       
-                    ┏━━━┫          ┃                       
-            'ymap'╺━┛   ┗━━━━━━━━━━┛                       
-            video                                          
"""
@dataclass(repr=False, eq=False)
class dnn_classify(Filter, AVOptions.dnn_classify, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ DNN_CLASSIFY ┣━━━━━╸'default'      
-         video        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class dnn_detect(Filter, AVOptions.dnn_detect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ DNN_DETECT ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class dnn_processing(Filter, AVOptions.dnn_processing, inputs_count=1, outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━━━┓                    
-                     ┃                ┃                    
-      'default'╺━━━━━┫ DNN_PROCESSING ┣━━━━━╸'default'     
-        video        ┃                ┃        video       
-                     ┗━━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class doubleweave(Filter, AVOptions._double_weave, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ DOUBLEWEAVE ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class drawbox(Filter, AVOptions.drawbox, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ DRAWBOX ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class drawgraph(Filter, AVOptions._a_drawgraph, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ DRAWGRAPH ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class drawgrid(Filter, AVOptions.drawgrid, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ DRAWGRID ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class drawtext(Filter, AVOptions.drawtext, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ DRAWTEXT ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class edgedetect(Filter, AVOptions.edgedetect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ EDGEDETECT ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class elbg(Filter, AVOptions.elbg, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ ELBG ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class entropy(Filter, AVOptions.entropy, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ ENTROPY ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class epx(Filter, AVOptions.epx, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ EPX ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class eq(Filter, AVOptions.eq, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━┓                          
-                           ┃    ┃                          
-            'default'╺━━━━━┫ EQ ┣━━━━━╸'default'           
-              video        ┃    ┃        video             
-                           ┗━━━━┛                          
-                                                           
"""
@dataclass(repr=False, eq=False)
class erosion(Filter, AVOptions.erosion_dilation, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ EROSION ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class estdif(Filter, AVOptions.estdif, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ESTDIF ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class exposure(Filter, AVOptions.exposure, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ EXPOSURE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class extractplanes(Filter, AVOptions.extractplanes, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ EXTRACTPLANES ┣━━━━━╸'dynamic'     
-         video        ┃               ┃                    
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class fade(Filter, AVOptions.fade, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ FADE ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class feedback(Filter, AVOptions.feedback, inputs_count=2, outputs_count=2):
    """
-                                                           
-         'default'╺━┓   ┏━━━━━━━━━━┓  ┏━━╸'default'        
-           video    ┗━━━┫          ┣━━┛     video          
-                        ┃          ┃                       
-                        ┃ FEEDBACK ┃                       
-                        ┃          ┃                       
-                    ┏━━━┫          ┣━━┓                    
-          'feedin'╺━┛   ┗━━━━━━━━━━┛  ┗━━╸'feedout'        
-            video                           video          
"""
@dataclass(repr=False, eq=False)
class fftdnoiz(Filter, AVOptions.fftdnoiz, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ FFTDNOIZ ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class fftfilt(Filter, AVOptions.fftfilt, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ FFTFILT ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class field(Filter, AVOptions.field, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ FIELD ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class fieldhint(Filter, AVOptions.fieldhint, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ FIELDHINT ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class fieldmatch(Filter, AVOptions.fieldmatch, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━┓                       
-                      ┃            ┃                       
-       'dynamic'╺━━━━━┫ FIELDMATCH ┣━━━━━╸'default'        
-                      ┃            ┃        video          
-                      ┗━━━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class fieldorder(Filter, AVOptions.fieldorder, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ FIELDORDER ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class fillborders(Filter, AVOptions.fillborders, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ FILLBORDERS ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class find_rect(Filter, AVOptions.find_rect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ FIND_RECT ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class floodfill(Filter, AVOptions.floodfill, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ FLOODFILL ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class format(Filter, AVOptions._no_format, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ FORMAT ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class fps(Filter, AVOptions.fps, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ FPS ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class framepack(Filter, AVOptions.framepack, inputs_count=2, outputs_count=1):
    """
-                                                           
-            'left'╺━┓   ┏━━━━━━━━━━━┓                      
-            video   ┗━━━┫           ┃                      
-                        ┃           ┃                      
-                        ┃ FRAMEPACK ┣━━━━━╸'packed'        
-                        ┃           ┃       video          
-                    ┏━━━┫           ┃                      
-           'right'╺━┛   ┗━━━━━━━━━━━┛                      
-            video                                          
"""
@dataclass(repr=False, eq=False)
class framerate(Filter, AVOptions.framerate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ FRAMERATE ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class framestep(Filter, AVOptions.framestep, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ FRAMESTEP ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class freezedetect(Filter, AVOptions.freezedetect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ FREEZEDETECT ┣━━━━━╸'default'      
-         video        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class freezeframes(Filter, AVOptions.freezeframes, inputs_count=2, outputs_count=1):
    """
-                                                           
-        'source'╺━┓   ┏━━━━━━━━━━━━━━┓                     
-          video   ┗━━━┫              ┃                     
-                      ┃              ┃                     
-                      ┃ FREEZEFRAMES ┣━━━━━╸'default'      
-                      ┃              ┃        video        
-                  ┏━━━┫              ┃                     
-       'replace'╺━┛   ┗━━━━━━━━━━━━━━┛                     
-         video                                             
"""
@dataclass(repr=False, eq=False)
class frei0r(Filter, AVOptions.frei0r, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ FREI0R ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class fspp(Filter, AVOptions.fspp, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ FSPP ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class gblur(Filter, AVOptions.gblur, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ GBLUR ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class geq(Filter, AVOptions.geq, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ GEQ ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class gradfun(Filter, AVOptions.gradfun, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ GRADFUN ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class graphmonitor(Filter, AVOptions._a_graphmonitor, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ GRAPHMONITOR ┣━━━━━╸'default'      
-         video        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class grayworld(Filter, AVOptions.grayworld, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ GRAYWORLD ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class greyedge(Filter, AVOptions.greyedge, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ GREYEDGE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class guided(Filter, AVOptions.guided, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━┓                         
-                        ┃        ┃                         
-         'dynamic'╺━━━━━┫ GUIDED ┣━━━━━╸'default'          
-                        ┃        ┃        video            
-                        ┗━━━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class haldclut(Filter, AVOptions.framesync, AVOptions.haldclut, inputs_count=2, outputs_count=1):
    """
-                                                           
-           'main'╺━┓   ┏━━━━━━━━━━┓                        
-            video  ┗━━━┫          ┃                        
-                       ┃          ┃                        
-                       ┃ HALDCLUT ┣━━━━━╸'default'         
-                       ┃          ┃        video           
-                   ┏━━━┫          ┃                        
-           'clut'╺━┛   ┗━━━━━━━━━━┛                        
-            video                                          
"""
@dataclass(repr=False, eq=False)
class hflip(Filter, AVOptions.hflip, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ HFLIP ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class histeq(Filter, AVOptions.histeq, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ HISTEQ ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class histogram(Filter, AVOptions.histogram, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ HISTOGRAM ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class hqdn3d(Filter, AVOptions.hqdn3d, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ HQDN3D ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class hqx(Filter, AVOptions.hqx, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ HQX ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class hstack(Filter, AVOptions._h_v_stack, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━┓                         
-                        ┃        ┃                         
-         'dynamic'╺━━━━━┫ HSTACK ┣━━━━━╸'default'          
-                        ┃        ┃        video            
-                        ┗━━━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class hsvhold(Filter, AVOptions.hsvhold, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ HSVHOLD ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class hsvkey(Filter, AVOptions.hsvkey, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ HSVKEY ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class hue(Filter, AVOptions.hue, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ HUE ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class huesaturation(Filter, AVOptions.huesaturation, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ HUESATURATION ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class hwdownload(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ HWDOWNLOAD ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class hwmap(Filter, AVOptions.hwmap, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ HWMAP ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class hwupload(Filter, AVOptions.hwupload, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ HWUPLOAD ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class hysteresis(Filter, AVOptions.framesync, AVOptions.hysteresis, inputs_count=2, outputs_count=1):
    """
-                                                           
-          'base'╺━┓   ┏━━━━━━━━━━━━┓                       
-           video  ┗━━━┫            ┃                       
-                      ┃            ┃                       
-                      ┃ HYSTERESIS ┣━━━━━╸'default'        
-                      ┃            ┃        video          
-                  ┏━━━┫            ┃                       
-           'alt'╺━┛   ┗━━━━━━━━━━━━┛                       
-           video                                           
"""
@dataclass(repr=False, eq=False)
class identity(Filter, AVOptions.framesync, AVOptions.identity, inputs_count=2, outputs_count=1):
    """
-                                                           
-             'main'╺━┓   ┏━━━━━━━━━━┓                      
-             video   ┗━━━┫          ┃                      
-                         ┃          ┃                      
-                         ┃ IDENTITY ┣━━━━━╸'default'       
-                         ┃          ┃        video         
-                     ┏━━━┫          ┃                      
-        'reference'╺━┛   ┗━━━━━━━━━━┛                      
-           video                                           
"""
@dataclass(repr=False, eq=False)
class idet(Filter, AVOptions.idet, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ IDET ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class il(Filter, AVOptions.il, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━┓                          
-                           ┃    ┃                          
-            'default'╺━━━━━┫ IL ┣━━━━━╸'default'           
-              video        ┃    ┃        video             
-                           ┗━━━━┛                          
-                                                           
"""
@dataclass(repr=False, eq=False)
class inflate(Filter, AVOptions.deflate_inflate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ INFLATE ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class interlace(Filter, AVOptions.interlace, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ INTERLACE ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class interleave(Filter, AVOptions.interleave, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━┓                       
-                      ┃            ┃                       
-       'dynamic'╺━━━━━┫ INTERLEAVE ┣━━━━━╸'default'        
-                      ┃            ┃        video          
-                      ┗━━━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class kerndeint(Filter, AVOptions.kerndeint, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ KERNDEINT ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class kirsch(Filter, AVOptions.kirsch_prewitt_roberts_scharr_sobel, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ KIRSCH ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class lagfun(Filter, AVOptions.lagfun, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ LAGFUN ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class latency(Filter, inputs_count=1, outputs_count=2):
    """
-                                                           
-     ╺━━━━┓  ┏━━╸'default'                                 
-          ┣━━┛     video                                   
-          ┃                                                
-     ENCY ┃                                                
-          ┃                                                
-          ┣━━┓                                             
-     ╺━━━━┛  ┗━━╸'This'                                    
-     ort for timeline through the 'enable' option.         
"""
@dataclass(repr=False, eq=False)
class lenscorrection(Filter, AVOptions.lenscorrection, inputs_count=1, outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━━━┓                    
-                     ┃                ┃                    
-      'default'╺━━━━━┫ LENSCORRECTION ┣━━━━━╸'default'     
-        video        ┃                ┃        video       
-                     ┗━━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class libvmaf(Filter, AVOptions.framesync, AVOptions.libvmaf, inputs_count=2, outputs_count=1):
    """
-                                                           
-             'main'╺━┓   ┏━━━━━━━━━┓                       
-              video  ┗━━━┫         ┃                       
-                         ┃         ┃                       
-                         ┃ LIBVMAF ┣━━━━━╸'default'        
-                         ┃         ┃        video          
-                     ┏━━━┫         ┃                       
-        'reference'╺━┛   ┗━━━━━━━━━┛                       
-           video                                           
"""
@dataclass(repr=False, eq=False)
class limitdiff(Filter, AVOptions.limitdiff, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━┓                        
-                      ┃           ┃                        
-       'dynamic'╺━━━━━┫ LIMITDIFF ┣━━━━━╸'default'         
-                      ┃           ┃        video           
-                      ┗━━━━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class limiter(Filter, AVOptions.limiter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ LIMITER ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class loop(Filter, AVOptions.loop, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ LOOP ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class lumakey(Filter, AVOptions.lumakey, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ LUMAKEY ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class lut(Filter, AVOptions.lut_lutyuv_lutrgb, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ LUT ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class lut1d(Filter, AVOptions.lut1d, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ LUT1D ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class lut2(Filter, AVOptions.framesync, AVOptions.lut2, inputs_count=2, outputs_count=1):
    """
-                                                           
-             'srcx'╺━┓   ┏━━━━━━┓                          
-              video  ┗━━━┫      ┃                          
-                         ┃      ┃                          
-                         ┃ LUT2 ┣━━━━━╸'default'           
-                         ┃      ┃        video             
-                     ┏━━━┫      ┃                          
-             'srcy'╺━┛   ┗━━━━━━┛                          
-              video                                        
"""
@dataclass(repr=False, eq=False)
class lut3d(Filter, AVOptions.lut3d, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ LUT3D ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class lutrgb(Filter, AVOptions.lut_lutyuv_lutrgb, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ LUTRGB ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class lutyuv(Filter, AVOptions.lut_lutyuv_lutrgb, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ LUTYUV ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class maskedclamp(Filter, AVOptions.maskedclamp, inputs_count=3, outputs_count=1):
    """
-                                                           
-          'base'╺━┓   ┏━━━━━━━━━━━━━┓                      
-           video  ┗━━━┫             ┃                      
-                      ┃             ┃                      
-                      ┃             ┃                      
-          'dark'╺━━━━━┫ MASKEDCLAMP ┣━━━━━╸'default'       
-           video      ┃             ┃        video         
-                      ┃             ┃                      
-                  ┏━━━┫             ┃                      
-        'bright'╺━┛   ┗━━━━━━━━━━━━━┛                      
-          video                                            
"""
@dataclass(repr=False, eq=False)
class maskedmax(Filter, AVOptions.masked_min_max_, inputs_count=3, outputs_count=1):
    """
-                                                           
-          'source'╺━┓   ┏━━━━━━━━━━━┓                      
-           video    ┗━━━┫           ┃                      
-                        ┃           ┃                      
-                        ┃           ┃                      
-         'filter1'╺━━━━━┫ MASKEDMAX ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┃           ┃                      
-                    ┏━━━┫           ┃                      
-         'filter2'╺━┛   ┗━━━━━━━━━━━┛                      
-           video                                           
"""
@dataclass(repr=False, eq=False)
class maskedmerge(Filter, AVOptions.maskedmerge, inputs_count=3, outputs_count=1):
    """
-                                                           
-           'base'╺━┓   ┏━━━━━━━━━━━━━┓                     
-           video   ┗━━━┫             ┃                     
-                       ┃             ┃                     
-                       ┃             ┃                     
-        'overlay'╺━━━━━┫ MASKEDMERGE ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┃             ┃                     
-                   ┏━━━┫             ┃                     
-           'mask'╺━┛   ┗━━━━━━━━━━━━━┛                     
-           video                                           
"""
@dataclass(repr=False, eq=False)
class maskedmin(Filter, AVOptions.masked_min_max_, inputs_count=3, outputs_count=1):
    """
-                                                           
-          'source'╺━┓   ┏━━━━━━━━━━━┓                      
-           video    ┗━━━┫           ┃                      
-                        ┃           ┃                      
-                        ┃           ┃                      
-         'filter1'╺━━━━━┫ MASKEDMIN ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┃           ┃                      
-                    ┏━━━┫           ┃                      
-         'filter2'╺━┛   ┗━━━━━━━━━━━┛                      
-           video                                           
"""
@dataclass(repr=False, eq=False)
class maskedthreshold(Filter, AVOptions.maskedthreshold, inputs_count=2, outputs_count=1):
    """
-                                                           
-       'source'╺━┓   ┏━━━━━━━━━━━━━━━━━┓                   
-         video   ┗━━━┫                 ┃                   
-                     ┃                 ┃                   
-                     ┃ MASKEDTHRESHOLD ┣━━━━━╸'default'    
-                     ┃                 ┃        video      
-                 ┏━━━┫                 ┃                   
-     'reference╺━┛   ┗━━━━━━━━━━━━━━━━━┛                   
-       video                                               
"""
@dataclass(repr=False, eq=False)
class maskfun(Filter, AVOptions.maskfun, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ MASKFUN ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class median(Filter, AVOptions.median, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ MEDIAN ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class mergeplanes(Filter, AVOptions.mergeplanes, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━┓                       
-                     ┃             ┃                       
-      'dynamic'╺━━━━━┫ MERGEPLANES ┣━━━━━╸'default'        
-                     ┃             ┃        video          
-                     ┗━━━━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class mestimate(Filter, AVOptions.mestimate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ MESTIMATE ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class metadata(Filter, AVOptions.metadata, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ METADATA ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class midequalizer(Filter, AVOptions.midequalizer, inputs_count=2, outputs_count=1):
    """
-                                                           
-          'in0'╺━┓   ┏━━━━━━━━━━━━━━┓                      
-          video  ┗━━━┫              ┃                      
-                     ┃              ┃                      
-                     ┃ MIDEQUALIZER ┣━━━━━╸'default'       
-                     ┃              ┃        video         
-                 ┏━━━┫              ┃                      
-          'in1'╺━┛   ┗━━━━━━━━━━━━━━┛                      
-          video                                            
"""
@dataclass(repr=False, eq=False)
class minterpolate(Filter, AVOptions.minterpolate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ MINTERPOLATE ┣━━━━━╸'default'      
-         video        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class mix(Filter, AVOptions.mix, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                         ┏━━━━━┓                           
-                         ┃     ┃                           
-          'dynamic'╺━━━━━┫ MIX ┣━━━━━╸'default'            
-                         ┃     ┃        video              
-                         ┗━━━━━┛                           
-                                                           
"""
@dataclass(repr=False, eq=False)
class monochrome(Filter, AVOptions.monochrome, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ MONOCHROME ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class morpho(Filter, AVOptions.framesync, AVOptions.morpho, inputs_count=2, outputs_count=1):
    """
-                                                           
-           'default'╺━┓   ┏━━━━━━━━┓                       
-             video    ┗━━━┫        ┃                       
-                          ┃        ┃                       
-                          ┃ MORPHO ┣━━━━━╸'default'        
-                          ┃        ┃        video          
-                      ┏━━━┫        ┃                       
-         'structure'╺━┛   ┗━━━━━━━━┛                       
-            video                                          
"""
@dataclass(repr=False, eq=False)
class mpdecimate(Filter, AVOptions.mpdecimate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ MPDECIMATE ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class msad(Filter, AVOptions.framesync, AVOptions.msad, inputs_count=2, outputs_count=1):
    """
-                                                           
-               'main'╺━┓   ┏━━━━━━┓                        
-               video   ┗━━━┫      ┃                        
-                           ┃      ┃                        
-                           ┃ MSAD ┣━━━━━╸'default'         
-                           ┃      ┃        video           
-                       ┏━━━┫      ┃                        
-          'reference'╺━┛   ┗━━━━━━┛                        
-             video                                         
"""
@dataclass(repr=False, eq=False)
class multiply(Filter, AVOptions.multiply, inputs_count=2, outputs_count=1):
    """
-                                                           
-          'source'╺━┓   ┏━━━━━━━━━━┓                       
-           video    ┗━━━┫          ┃                       
-                        ┃          ┃                       
-                        ┃ MULTIPLY ┣━━━━━╸'default'        
-                        ┃          ┃        video          
-                    ┏━━━┫          ┃                       
-          'factor'╺━┛   ┗━━━━━━━━━━┛                       
-           video                                           
"""
@dataclass(repr=False, eq=False)
class negate(Filter, AVOptions.negate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ NEGATE ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class nlmeans(Filter, AVOptions.nlmeans, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ NLMEANS ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class nnedi(Filter, AVOptions.nnedi, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ NNEDI ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class noformat(Filter, AVOptions._no_format, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ NOFORMAT ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class noise(Filter, AVOptions.noise, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ NOISE ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class normalize(Filter, AVOptions.normalize, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ NORMALIZE ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class null(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ NULL ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class ocr(Filter, AVOptions.ocr, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ OCR ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class oscilloscope(Filter, AVOptions.oscilloscope, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ OSCILLOSCOPE ┣━━━━━╸'default'      
-         video        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class overlay(Filter, AVOptions.framesync, AVOptions.overlay, inputs_count=2, outputs_count=1):
    """
-                                                           
-             'main'╺━┓   ┏━━━━━━━━━┓                       
-             video   ┗━━━┫         ┃                       
-                         ┃         ┃                       
-                         ┃ OVERLAY ┣━━━━━╸'default'        
-                         ┃         ┃        video          
-                     ┏━━━┫         ┃                       
-          'overlay'╺━┛   ┗━━━━━━━━━┛                       
-            video                                          
"""
@dataclass(repr=False, eq=False)
class owdenoise(Filter, AVOptions.owdenoise, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ OWDENOISE ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class pad(Filter, AVOptions.pad, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ PAD ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class palettegen(Filter, AVOptions.palettegen, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ PALETTEGEN ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class paletteuse(Filter, AVOptions.paletteuse, inputs_count=2, outputs_count=1):
    """
-                                                           
-        'default'╺━┓   ┏━━━━━━━━━━━━┓                      
-          video    ┗━━━┫            ┃                      
-                       ┃            ┃                      
-                       ┃ PALETTEUSE ┣━━━━━╸'default'       
-                       ┃            ┃        video         
-                   ┏━━━┫            ┃                      
-        'palette'╺━┛   ┗━━━━━━━━━━━━┛                      
-          video                                            
"""
@dataclass(repr=False, eq=False)
class perms(Filter, AVOptions._a_perms, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ PERMS ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class perspective(Filter, AVOptions.perspective, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ PERSPECTIVE ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class phase(Filter, AVOptions.phase, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ PHASE ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class photosensitivity(Filter, AVOptions.photosensitivity, inputs_count=1, outputs_count=1):
    """
-                                                           
-                    ┏━━━━━━━━━━━━━━━━━━┓                   
-                    ┃                  ┃                   
-     'default'╺━━━━━┫ PHOTOSENSITIVITY ┣━━━━━╸'default'    
-       video        ┃                  ┃        video      
-                    ┗━━━━━━━━━━━━━━━━━━┛                   
-                                                           
"""
@dataclass(repr=False, eq=False)
class pixdesctest(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ PIXDESCTEST ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class pixelize(Filter, AVOptions.pixelize, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ PIXELIZE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class pixscope(Filter, AVOptions.pixscope, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ PIXSCOPE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class pp(Filter, AVOptions.pp, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━┓                          
-                           ┃    ┃                          
-            'default'╺━━━━━┫ PP ┣━━━━━╸'default'           
-              video        ┃    ┃        video             
-                           ┗━━━━┛                          
-                                                           
"""
@dataclass(repr=False, eq=False)
class pp7(Filter, AVOptions.pp7, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ PP7 ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class premultiply(Filter, AVOptions._un_premultiply, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━┓                       
-                     ┃             ┃                       
-      'dynamic'╺━━━━━┫ PREMULTIPLY ┣━━━━━╸'default'        
-                     ┃             ┃        video          
-                     ┗━━━━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class prewitt(Filter, AVOptions.kirsch_prewitt_roberts_scharr_sobel, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ PREWITT ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class pseudocolor(Filter, AVOptions.pseudocolor, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ PSEUDOCOLOR ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class psnr(Filter, AVOptions.framesync, AVOptions.psnr, inputs_count=2, outputs_count=1):
    """
-                                                           
-               'main'╺━┓   ┏━━━━━━┓                        
-               video   ┗━━━┫      ┃                        
-                           ┃      ┃                        
-                           ┃ PSNR ┣━━━━━╸'default'         
-                           ┃      ┃        video           
-                       ┏━━━┫      ┃                        
-          'reference'╺━┛   ┗━━━━━━┛                        
-             video                                         
"""
@dataclass(repr=False, eq=False)
class pullup(Filter, AVOptions.pullup, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ PULLUP ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class qp(Filter, AVOptions.qp, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━┓                          
-                           ┃    ┃                          
-            'default'╺━━━━━┫ QP ┣━━━━━╸'default'           
-              video        ┃    ┃        video             
-                           ┗━━━━┛                          
-                                                           
"""
@dataclass(repr=False, eq=False)
class random(Filter, AVOptions.random, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ RANDOM ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class readeia608(Filter, AVOptions.readeia608, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ READEIA608 ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class readvitc(Filter, AVOptions.readvitc, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ READVITC ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class realtime(Filter, AVOptions._a_realtime, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ REALTIME ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class remap(Filter, AVOptions.remap, inputs_count=3, outputs_count=1):
    """
-                                                           
-           'source'╺━┓   ┏━━━━━━━┓                         
-             video   ┗━━━┫       ┃                         
-                         ┃       ┃                         
-                         ┃       ┃                         
-             'xmap'╺━━━━━┫ REMAP ┣━━━━━╸'default'          
-              video      ┃       ┃        video            
-                         ┃       ┃                         
-                     ┏━━━┫       ┃                         
-             'ymap'╺━┛   ┗━━━━━━━┛                         
-              video                                        
"""
@dataclass(repr=False, eq=False)
class removegrain(Filter, AVOptions.removegrain, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ REMOVEGRAIN ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class removelogo(Filter, AVOptions.removelogo, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ REMOVELOGO ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class repeatfields(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ REPEATFIELDS ┣━━━━━╸'default'      
-         video        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class reverse(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ REVERSE ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class rgbashift(Filter, AVOptions.rgbashift, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ RGBASHIFT ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class roberts(Filter, AVOptions.kirsch_prewitt_roberts_scharr_sobel, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ ROBERTS ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class rotate(Filter, AVOptions.rotate, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ROTATE ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class sab(Filter, AVOptions.sab, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ SAB ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class scale(Filter, AVOptions.SWScaler, AVOptions.scale_2ref_, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ SCALE ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class scale2ref(Filter, AVOptions.SWScaler, AVOptions.scale_2ref_, inputs_count=2, outputs_count=2):
    """
-                                                           
-         'default'╺━┓   ┏━━━━━━━━━━━┓  ┏━━╸'default'       
-           video    ┗━━━┫           ┣━━┛     video         
-                        ┃           ┃                      
-                        ┃ SCALE2REF ┃                      
-                        ┃           ┃                      
-                    ┏━━━┫           ┣━━┓                   
-             'ref'╺━┛   ┗━━━━━━━━━━━┛  ┗━━╸'ref'           
-             video                         video           
"""
@dataclass(repr=False, eq=False)
class scdet(Filter, AVOptions.scdet, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ SCDET ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class scharr(Filter, AVOptions.kirsch_prewitt_roberts_scharr_sobel, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ SCHARR ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class scroll(Filter, AVOptions.scroll, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ SCROLL ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class segment(Filter, AVOptions.segment, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ SEGMENT ┣━━━━━╸'dynamic'        
-            video        ┃         ┃                       
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class select(Filter, AVOptions.select, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ SELECT ┣━━━━━╸'dynamic'         
-            video        ┃        ┃                        
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class selectivecolor(Filter, AVOptions.selectivecolor, inputs_count=1, outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━━━┓                    
-                     ┃                ┃                    
-      'default'╺━━━━━┫ SELECTIVECOLOR ┣━━━━━╸'default'     
-        video        ┃                ┃        video       
-                     ┗━━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class sendcmd(Filter, AVOptions._a_sendcmd, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ SENDCMD ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class separatefields(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━━━┓                    
-                     ┃                ┃                    
-      'default'╺━━━━━┫ SEPARATEFIELDS ┣━━━━━╸'default'     
-        video        ┃                ┃        video       
-                     ┗━━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class setdar(Filter, AVOptions.setdar, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ SETDAR ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class setfield(Filter, AVOptions.setfield, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ SETFIELD ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class setparams(Filter, AVOptions.setparams, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ SETPARAMS ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class setpts(Filter, AVOptions.setpts, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ SETPTS ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class setrange(Filter, AVOptions.setrange, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ SETRANGE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class setsar(Filter, AVOptions.setsar, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ SETSAR ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class settb(Filter, AVOptions.settb, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ SETTB ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class shear(Filter, AVOptions.shear, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ SHEAR ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class showinfo(Filter, AVOptions.showinfo, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ SHOWINFO ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class showpalette(Filter, AVOptions.showpalette, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ SHOWPALETTE ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class shuffleframes(Filter, AVOptions.shuffleframes, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ SHUFFLEFRAMES ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class shufflepixels(Filter, AVOptions.shufflepixels, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ SHUFFLEPIXELS ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class shuffleplanes(Filter, AVOptions.shuffleplanes, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ SHUFFLEPLANES ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class sidedata(Filter, AVOptions.sidedata, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ SIDEDATA ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class signalstats(Filter, AVOptions.signalstats, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ SIGNALSTATS ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class signature(Filter, AVOptions.signature, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━┓                        
-                      ┃           ┃                        
-       'dynamic'╺━━━━━┫ SIGNATURE ┣━━━━━╸'default'         
-                      ┃           ┃        video           
-                      ┗━━━━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class siti(Filter, AVOptions.siti, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ SITI ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class smartblur(Filter, AVOptions.smartblur, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ SMARTBLUR ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class sobel(Filter, AVOptions.kirsch_prewitt_roberts_scharr_sobel, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ SOBEL ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class split(Filter, AVOptions._a_split, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ SPLIT ┣━━━━━╸'dynamic'         
-             video        ┃       ┃                        
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class spp(Filter, AVOptions.AVDCT, AVOptions.spp, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ SPP ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class sr(Filter, AVOptions.sr, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━┓                          
-                           ┃    ┃                          
-            'default'╺━━━━━┫ SR ┣━━━━━╸'default'           
-              video        ┃    ┃        video             
-                           ┗━━━━┛                          
-                                                           
"""
@dataclass(repr=False, eq=False)
class ssim(Filter, AVOptions.framesync, AVOptions.ssim, inputs_count=2, outputs_count=1):
    """
-                                                           
-               'main'╺━┓   ┏━━━━━━┓                        
-               video   ┗━━━┫      ┃                        
-                           ┃      ┃                        
-                           ┃ SSIM ┣━━━━━╸'default'         
-                           ┃      ┃        video           
-                       ┏━━━┫      ┃                        
-          'reference'╺━┛   ┗━━━━━━┛                        
-             video                                         
"""
@dataclass(repr=False, eq=False)
class ssim360(Filter, AVOptions.framesync, AVOptions.ssim360, inputs_count=2, outputs_count=1):
    """
-                                                           
-             'main'╺━┓   ┏━━━━━━━━━┓                       
-              video  ┗━━━┫         ┃                       
-                         ┃         ┃                       
-                         ┃ SSIM360 ┣━━━━━╸'default'        
-                         ┃         ┃        video          
-                     ┏━━━┫         ┃                       
-        'reference'╺━┛   ┗━━━━━━━━━┛                       
-           video                                           
"""
@dataclass(repr=False, eq=False)
class stereo3d(Filter, AVOptions.stereo3d, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ STEREO3D ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class streamselect(Filter, AVOptions._a_streamselect, inputs_count="dynamic", outputs_count="dynamic"):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━┓                      
-                     ┃              ┃                      
-      'dynamic'╺━━━━━┫ STREAMSELECT ┣━━━━━╸'dynamic'       
-                     ┃              ┃                      
-                     ┗━━━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class subtitles(Filter, AVOptions.subtitles, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ SUBTITLES ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class super2xsai(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ SUPER2XSAI ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class swaprect(Filter, AVOptions.swaprect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ SWAPRECT ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class swapuv(Filter, AVOptions.swapuv, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ SWAPUV ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class tblend(Filter, AVOptions.tblend, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ TBLEND ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class telecine(Filter, AVOptions.telecine, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ TELECINE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class thistogram(Filter, AVOptions.thistogram, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ THISTOGRAM ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class threshold(Filter, AVOptions.threshold, inputs_count=4, outputs_count=1):
    """
-                                                           
-         'default'╺━┓   ┏━━━━━━━━━━━┓                      
-           video    ┗━━━┫           ┃                      
-                        ┃           ┃                      
-       'threshold'╺━━━━━┫           ┃                      
-          video         ┃           ┃                      
-                        ┃ THRESHOLD ┣━━━━━╸'default'       
-                        ┃           ┃        video         
-             'min'╺━━━━━┫           ┃                      
-             video      ┃           ┃                      
-                    ┏━━━┫           ┃                      
-             'max'╺━┛   ┗━━━━━━━━━━━┛                      
-             video                                         
"""
@dataclass(repr=False, eq=False)
class thumbnail(Filter, AVOptions.thumbnail, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ THUMBNAIL ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class tile(Filter, AVOptions.tile, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ TILE ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class tinterlace(Filter, AVOptions.tinterlace, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ TINTERLACE ┣━━━━━╸'default'       
-          video        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class tlut2(Filter, AVOptions.tlut2, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ TLUT2 ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class tmedian(Filter, AVOptions.tmedian, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ TMEDIAN ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class tmidequalizer(Filter, AVOptions.tmidequalizer, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ TMIDEQUALIZER ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class tmix(Filter, AVOptions.tmix, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ TMIX ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class tonemap(Filter, AVOptions.tonemap, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ TONEMAP ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class tpad(Filter, AVOptions.tpad, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ TPAD ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class transpose(Filter, AVOptions.transpose, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ TRANSPOSE ┣━━━━━╸'default'       
-           video        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class trim(Filter, AVOptions.trim, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ TRIM ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class unpremultiply(Filter, AVOptions._un_premultiply, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                    ┏━━━━━━━━━━━━━━━┓                      
-                    ┃               ┃                      
-     'dynamic'╺━━━━━┫ UNPREMULTIPLY ┣━━━━━╸'default'       
-                    ┃               ┃        video         
-                    ┗━━━━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class unsharp(Filter, AVOptions.unsharp, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ UNSHARP ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class untile(Filter, AVOptions.untile, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ UNTILE ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class v360(Filter, AVOptions.v360, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ V360 ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class vaguedenoiser(Filter, AVOptions.vaguedenoiser, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ VAGUEDENOISER ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class varblur(Filter, AVOptions.framesync, AVOptions.varblur, inputs_count=2, outputs_count=1):
    """
-                                                           
-          'default'╺━┓   ┏━━━━━━━━━┓                       
-            video    ┗━━━┫         ┃                       
-                         ┃         ┃                       
-                         ┃ VARBLUR ┣━━━━━╸'default'        
-                         ┃         ┃        video          
-                     ┏━━━┫         ┃                       
-           'radius'╺━┛   ┗━━━━━━━━━┛                       
-            video                                          
"""
@dataclass(repr=False, eq=False)
class vectorscope(Filter, AVOptions.vectorscope, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ VECTORSCOPE ┣━━━━━╸'default'      
-          video        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class vflip(Filter, AVOptions.vflip, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ VFLIP ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class vfrdet(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ VFRDET ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class vibrance(Filter, AVOptions.vibrance, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ VIBRANCE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class vidstabdetect(Filter, AVOptions.vidstabdetect, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ VIDSTABDETECT ┣━━━━━╸'default'     
-         video        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class vidstabtransform(Filter, AVOptions.vidstabtransform, inputs_count=1, outputs_count=1):
    """
-                                                           
-                    ┏━━━━━━━━━━━━━━━━━━┓                   
-                    ┃                  ┃                   
-     'default'╺━━━━━┫ VIDSTABTRANSFORM ┣━━━━━╸'default'    
-       video        ┃                  ┃        video      
-                    ┗━━━━━━━━━━━━━━━━━━┛                   
-                                                           
"""
@dataclass(repr=False, eq=False)
class vif(Filter, AVOptions.framesync, AVOptions.vif, inputs_count=2, outputs_count=1):
    """
-                                                           
-               'main'╺━┓   ┏━━━━━┓                         
-                video  ┗━━━┫     ┃                         
-                           ┃     ┃                         
-                           ┃ VIF ┣━━━━━╸'default'          
-                           ┃     ┃        video            
-                       ┏━━━┫     ┃                         
-          'reference'╺━┛   ┗━━━━━┛                         
-             video                                         
"""
@dataclass(repr=False, eq=False)
class vignette(Filter, AVOptions.vignette, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ VIGNETTE ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class vmafmotion(Filter, AVOptions.vmafmotion, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━┓                     
-                        ┃            ┃                     
-       'reference'╺━━━━━┫ VMAFMOTION ┣━━━━━╸'default'      
-          video         ┃            ┃        video        
-                        ┗━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class vstack(Filter, AVOptions._h_v_stack, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━┓                         
-                        ┃        ┃                         
-         'dynamic'╺━━━━━┫ VSTACK ┣━━━━━╸'default'          
-                        ┃        ┃        video            
-                        ┗━━━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class w3fdif(Filter, AVOptions.w3fdif, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ W3FDIF ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class waveform(Filter, AVOptions.waveform, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ WAVEFORM ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class weave(Filter, AVOptions._double_weave, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ WEAVE ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class xbr(Filter, AVOptions.xbr, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ XBR ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class xcorrelate(Filter, AVOptions.framesync, AVOptions.xcorrelate, inputs_count=2, outputs_count=1):
    """
-                                                           
-         'primary'╺━┓   ┏━━━━━━━━━━━━┓                     
-           video    ┗━━━┫            ┃                     
-                        ┃            ┃                     
-                        ┃ XCORRELATE ┣━━━━━╸'default'      
-                        ┃            ┃        video        
-                    ┏━━━┫            ┃                     
-       'secondary'╺━┛   ┗━━━━━━━━━━━━┛                     
-          video                                            
"""
@dataclass(repr=False, eq=False)
class xfade(Filter, AVOptions.xfade, inputs_count=2, outputs_count=1):
    """
-                                                           
-             'main'╺━┓   ┏━━━━━━━┓                         
-              video  ┗━━━┫       ┃                         
-                         ┃       ┃                         
-                         ┃ XFADE ┣━━━━━╸'default'          
-                         ┃       ┃        video            
-                     ┏━━━┫       ┃                         
-            'xfade'╺━┛   ┗━━━━━━━┛                         
-             video                                         
"""
@dataclass(repr=False, eq=False)
class xmedian(Filter, AVOptions.framesync, AVOptions.xmedian, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━┓                         
-                       ┃         ┃                         
-        'dynamic'╺━━━━━┫ XMEDIAN ┣━━━━━╸'default'          
-                       ┃         ┃        video            
-                       ┗━━━━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class xstack(Filter, AVOptions.xstack, inputs_count="dynamic", outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━┓                         
-                        ┃        ┃                         
-         'dynamic'╺━━━━━┫ XSTACK ┣━━━━━╸'default'          
-                        ┃        ┃        video            
-                        ┗━━━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class yadif(Filter, AVOptions.yadif, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ YADIF ┣━━━━━╸'default'         
-             video        ┃       ┃        video           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class yadif_videotoolbox(Filter, AVOptions.yadif_videotoolbox, inputs_count=1, outputs_count=1):
    """
-                                                           
-                   ┏━━━━━━━━━━━━━━━━━━━━┓                  
-                   ┃                    ┃                  
-     'default╺━━━━━┫ YADIF_VIDEOTOOLBOX ┣━━━━━╸'default'   
-      video        ┃                    ┃        video     
-                   ┗━━━━━━━━━━━━━━━━━━━━┛                  
-                                                           
"""
@dataclass(repr=False, eq=False)
class yaepblur(Filter, AVOptions.yaepblur, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ YAEPBLUR ┣━━━━━╸'default'        
-           video        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class zmq(Filter, AVOptions._a_zmq, inputs_count=1, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━┓                         
-                           ┃     ┃                         
-            'default'╺━━━━━┫ ZMQ ┣━━━━━╸'default'          
-              video        ┃     ┃        video            
-                           ┗━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class zoompan(Filter, AVOptions.zoompan, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ ZOOMPAN ┣━━━━━╸'default'        
-            video        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class zscale(Filter, AVOptions.zscale, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━┓                        
-                         ┃        ┃                        
-          'default'╺━━━━━┫ ZSCALE ┣━━━━━╸'default'         
-            video        ┃        ┃        video           
-                         ┗━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class allrgb(Filter, AVOptions.allyuv_allrgb, inputs_count=0, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━━┓                       
-                          ┃        ┃                       
-              'none'╺━━━━━┫ ALLRGB ┣━━━━━╸'default'        
-           source filter  ┃        ┃        video          
-                          ┗━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class allyuv(Filter, AVOptions.allyuv_allrgb, inputs_count=0, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━━┓                       
-                          ┃        ┃                       
-              'none'╺━━━━━┫ ALLYUV ┣━━━━━╸'default'        
-           source filter  ┃        ┃        video          
-                          ┗━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class cellauto(Filter, AVOptions.cellauto, inputs_count=0, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━━┓                      
-                         ┃          ┃                      
-             'none'╺━━━━━┫ CELLAUTO ┣━━━━━╸'default'       
-          source filter  ┃          ┃        video         
-                         ┗━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class color(Filter, AVOptions.color, inputs_count=0, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━━━┓                       
-                           ┃       ┃                       
-               'none'╺━━━━━┫ COLOR ┣━━━━━╸'default'        
-           source filter   ┃       ┃        video          
-                           ┗━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorchart(Filter, AVOptions.colorchart, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━┓                     
-                        ┃            ┃                     
-            'none'╺━━━━━┫ COLORCHART ┣━━━━━╸'default'      
-         source filter  ┃            ┃        video        
-                        ┗━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class colorspectrum(Filter, AVOptions.colorspectrum, inputs_count=0, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━━━┓                   
-                       ┃               ┃                   
-           'none'╺━━━━━┫ COLORSPECTRUM ┣━━━━━╸'default'    
-       source filter   ┃               ┃        video      
-                       ┗━━━━━━━━━━━━━━━┛                   
-                                                           
"""
@dataclass(repr=False, eq=False)
class coreimagesrc(Filter, AVOptions.coreimagesrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━━┓                    
-                       ┃              ┃                    
-           'none'╺━━━━━┫ COREIMAGESRC ┣━━━━━╸'default'     
-        source filter  ┃              ┃        video       
-                       ┗━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class frei0r_src(Filter, AVOptions.frei0r_src, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━┓                     
-                        ┃            ┃                     
-            'none'╺━━━━━┫ FREI0R_SRC ┣━━━━━╸'default'      
-         source filter  ┃            ┃        video        
-                        ┗━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class gradients(Filter, AVOptions.gradients, inputs_count=0, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━━━┓                     
-                         ┃           ┃                     
-             'none'╺━━━━━┫ GRADIENTS ┣━━━━━╸'default'      
-         source filter   ┃           ┃        video        
-                         ┗━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class haldclutsrc(Filter, AVOptions.haldclutsrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━━┓                    
-                        ┃             ┃                    
-            'none'╺━━━━━┫ HALDCLUTSRC ┣━━━━━╸'default'     
-        source filter   ┃             ┃        video       
-                        ┗━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class life(Filter, AVOptions.life, inputs_count=0, outputs_count=1):
    """
-                                                           
-                           ┏━━━━━━┓                        
-                           ┃      ┃                        
-               'none'╺━━━━━┫ LIFE ┣━━━━━╸'default'         
-            source filter  ┃      ┃        video           
-                           ┗━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class mandelbrot(Filter, AVOptions.mandelbrot, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━┓                     
-                        ┃            ┃                     
-            'none'╺━━━━━┫ MANDELBROT ┣━━━━━╸'default'      
-         source filter  ┃            ┃        video        
-                        ┗━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class mptestsrc(Filter, AVOptions.mptestsrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━━━┓                     
-                         ┃           ┃                     
-             'none'╺━━━━━┫ MPTESTSRC ┣━━━━━╸'default'      
-         source filter   ┃           ┃        video        
-                         ┗━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class pal75bars(Filter, AVOptions.pal_75_100_bars, inputs_count=0, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━━━┓                     
-                         ┃           ┃                     
-             'none'╺━━━━━┫ PAL75BARS ┣━━━━━╸'default'      
-         source filter   ┃           ┃        video        
-                         ┗━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class pal100bars(Filter, AVOptions.pal_75_100_bars, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━┓                     
-                        ┃            ┃                     
-            'none'╺━━━━━┫ PAL100BARS ┣━━━━━╸'default'      
-         source filter  ┃            ┃        video        
-                        ┗━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class rgbtestsrc(Filter, AVOptions.rgbtestsrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━┓                     
-                        ┃            ┃                     
-            'none'╺━━━━━┫ RGBTESTSRC ┣━━━━━╸'default'      
-         source filter  ┃            ┃        video        
-                        ┗━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class sierpinski(Filter, AVOptions.sierpinski, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━┓                     
-                        ┃            ┃                     
-            'none'╺━━━━━┫ SIERPINSKI ┣━━━━━╸'default'      
-         source filter  ┃            ┃        video        
-                        ┗━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class smptebars(Filter, AVOptions.smpte_hd_bars, inputs_count=0, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━━━┓                     
-                         ┃           ┃                     
-             'none'╺━━━━━┫ SMPTEBARS ┣━━━━━╸'default'      
-         source filter   ┃           ┃        video        
-                         ┗━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class testsrc(Filter, AVOptions.testsrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━━━┓                      
-                          ┃         ┃                      
-              'none'╺━━━━━┫ TESTSRC ┣━━━━━╸'default'       
-          source filter   ┃         ┃        video         
-                          ┗━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class testsrc2(Filter, AVOptions.testsrc2, inputs_count=0, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━━┓                      
-                         ┃          ┃                      
-             'none'╺━━━━━┫ TESTSRC2 ┣━━━━━╸'default'       
-          source filter  ┃          ┃        video         
-                         ┗━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class nullsink(Filter, inputs_count=1, outputs_count=0):
    """
-                                                           
-                       ┏━━━━━━━━━━┓                        
-                       ┃          ┃                        
-        'default'╺━━━━━┫ NULLSINK ┣━━━━━╸'none'            
-          video        ┃          ┃   sink filter          
-                       ┗━━━━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class a3dscope(Filter, AVOptions.a3dscope, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━┓                       
-                        ┃          ┃                       
-         'default'╺━━━━━┫ A3DSCOPE ┣━━━━━╸'default'        
-           audio        ┃          ┃        video          
-                        ┗━━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class abitscope(Filter, AVOptions.abitscope, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ ABITSCOPE ┣━━━━━╸'default'       
-           audio        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class adrawgraph(Filter, AVOptions._a_drawgraph, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ ADRAWGRAPH ┣━━━━━╸'default'       
-          audio        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class agraphmonitor(Filter, AVOptions._a_graphmonitor, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━━┓                    
-                      ┃               ┃                    
-       'default'╺━━━━━┫ AGRAPHMONITOR ┣━━━━━╸'default'     
-         audio        ┃               ┃        video       
-                      ┗━━━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class nullsrc(Filter, AVOptions.nullsrc_yuvtestsrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━━━┓                      
-                          ┃         ┃                      
-              'none'╺━━━━━┫ NULLSRC ┣━━━━━╸'default'       
-          source filter   ┃         ┃        video         
-                          ┗━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class showcqt(Filter, AVOptions.showcqt, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ SHOWCQT ┣━━━━━╸'default'        
-            audio        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class aphasemeter(Filter, AVOptions.aphasemeter, inputs_count=1, outputs_count="dynamic"):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ APHASEMETER ┣━━━━━╸'dynamic'      
-          audio        ┃             ┃                     
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class yuvtestsrc(Filter, AVOptions.nullsrc_yuvtestsrc, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━┓                     
-                        ┃            ┃                     
-            'none'╺━━━━━┫ YUVTESTSRC ┣━━━━━╸'default'      
-         source filter  ┃            ┃        video        
-                        ┗━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class avectorscope(Filter, AVOptions.avectorscope, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ AVECTORSCOPE ┣━━━━━╸'default'      
-         audio        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class smptehdbars(Filter, AVOptions.smpte_hd_bars, inputs_count=0, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━━━┓                    
-                        ┃             ┃                    
-            'none'╺━━━━━┫ SMPTEHDBARS ┣━━━━━╸'default'     
-        source filter   ┃             ┃        video       
-                        ┗━━━━━━━━━━━━━┛                    
-                                                           
"""
@dataclass(repr=False, eq=False)
class amovie(Filter, AVOptions._a_movie, inputs_count=0, outputs_count="dynamic"):
    """
-                                                           
-                          ┏━━━━━━━━┓                       
-                          ┃        ┃                       
-              'none'╺━━━━━┫ AMOVIE ┣━━━━━╸'dynamic'        
-           source filter  ┃        ┃                       
-                          ┗━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class showfreqs(Filter, AVOptions.showfreqs, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ SHOWFREQS ┣━━━━━╸'default'       
-           audio        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class showspectrumpic(Filter, AVOptions.showspectrumpic, inputs_count=1, outputs_count=1):
    """
-                                                           
-                     ┏━━━━━━━━━━━━━━━━━┓                   
-                     ┃                 ┃                   
-      'default'╺━━━━━┫ SHOWSPECTRUMPIC ┣━━━━━╸'default'    
-        audio        ┃                 ┃        video      
-                     ┗━━━━━━━━━━━━━━━━━┛                   
-                                                           
"""
@dataclass(repr=False, eq=False)
class showwaves(Filter, AVOptions.showwaves, inputs_count=1, outputs_count=1):
    """
-                                                           
-                        ┏━━━━━━━━━━━┓                      
-                        ┃           ┃                      
-         'default'╺━━━━━┫ SHOWWAVES ┣━━━━━╸'default'       
-           audio        ┃           ┃        video         
-                        ┗━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class spectrumsynth(Filter, AVOptions.spectrumsynth, inputs_count=2, outputs_count=1):
    """
-                                                           
-     'magnitude'╺━┓   ┏━━━━━━━━━━━━━━━┓                    
-        video     ┗━━━┫               ┃                    
-                      ┃               ┃                    
-                      ┃ SPECTRUMSYNTH ┣━━━━━╸'default'     
-                      ┃               ┃        audio       
-                  ┏━━━┫               ┃                    
-         'phase'╺━┛   ┗━━━━━━━━━━━━━━━┛                    
-          video                                            
"""
@dataclass(repr=False, eq=False)
class ahistogram(Filter, AVOptions.ahistogram, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ AHISTOGRAM ┣━━━━━╸'default'       
-          audio        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class buffer(Filter, AVOptions.buffer, inputs_count=0, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━━┓                       
-                          ┃        ┃                       
-              'none'╺━━━━━┫ BUFFER ┣━━━━━╸'default'        
-           source filter  ┃        ┃        video          
-                          ┗━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class showcwt(Filter, AVOptions.showcwt, inputs_count=1, outputs_count=1):
    """
-                                                           
-                         ┏━━━━━━━━━┓                       
-                         ┃         ┃                       
-          'default'╺━━━━━┫ SHOWCWT ┣━━━━━╸'default'        
-            audio        ┃         ┃        video          
-                         ┗━━━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class showwavespic(Filter, AVOptions.showwavespic, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ SHOWWAVESPIC ┣━━━━━╸'default'      
-         audio        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class concat(Filter, AVOptions.concat, inputs_count="dynamic", outputs_count="dynamic"):
    """
-                                                           
-                        ┏━━━━━━━━┓                         
-                        ┃        ┃                         
-         'dynamic'╺━━━━━┫ CONCAT ┣━━━━━╸'dynamic'          
-                        ┃        ┃                         
-                        ┗━━━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class avsynctest(Filter, AVOptions.avsynctest, inputs_count=0, outputs_count=2):
    """
-                                                           
-                         ┏━━━━━━━━━━━━┓  ┏━━╸'audio'       
-                         ┃            ┣━━┛                 
-                         ┃            ┃                    
-             'none'╺━━━━━┫ AVSYNCTEST ┃                    
-          source filter  ┃            ┃                    
-                         ┃            ┣━━┓                 
-                         ┗━━━━━━━━━━━━┛  ┗━━╸'video'       
-                                                           
"""
@dataclass(repr=False, eq=False)
class showvolume(Filter, AVOptions.showvolume, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━┓                      
-                       ┃            ┃                      
-        'default'╺━━━━━┫ SHOWVOLUME ┣━━━━━╸'default'       
-          audio        ┃            ┃        video         
-                       ┗━━━━━━━━━━━━┛                      
-                                                           
"""
@dataclass(repr=False, eq=False)
class afifo(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━┓                        
-                          ┃       ┃                        
-           'default'╺━━━━━┫ AFIFO ┣━━━━━╸'default'         
-             audio        ┃       ┃        audio           
-                          ┗━━━━━━━┛                        
-                                                           
"""
@dataclass(repr=False, eq=False)
class showspectrum(Filter, AVOptions.showspectrum, inputs_count=1, outputs_count=1):
    """
-                                                           
-                      ┏━━━━━━━━━━━━━━┓                     
-                      ┃              ┃                     
-       'default'╺━━━━━┫ SHOWSPECTRUM ┣━━━━━╸'default'      
-         audio        ┃              ┃        video        
-                      ┗━━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class movie(Filter, AVOptions._a_movie, inputs_count=0, outputs_count="dynamic"):
    """
-                                                           
-                           ┏━━━━━━━┓                       
-                           ┃       ┃                       
-               'none'╺━━━━━┫ MOVIE ┣━━━━━╸'dynamic'        
-           source filter   ┃       ┃                       
-                           ┗━━━━━━━┛                       
-                                                           
"""
@dataclass(repr=False, eq=False)
class showspatial(Filter, AVOptions.showspatial, inputs_count=1, outputs_count=1):
    """
-                                                           
-                       ┏━━━━━━━━━━━━━┓                     
-                       ┃             ┃                     
-        'default'╺━━━━━┫ SHOWSPATIAL ┣━━━━━╸'default'      
-          audio        ┃             ┃        video        
-                       ┗━━━━━━━━━━━━━┛                     
-                                                           
"""
@dataclass(repr=False, eq=False)
class fifo(Filter, inputs_count=1, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━┓                         
-                          ┃      ┃                         
-           'default'╺━━━━━┫ FIFO ┣━━━━━╸'default'          
-             video        ┃      ┃        video            
-                          ┗━━━━━━┛                         
-                                                           
"""
@dataclass(repr=False, eq=False)
class abuffer(Filter, AVOptions.abuffer, inputs_count=0, outputs_count=1):
    """
-                                                           
-                          ┏━━━━━━━━━┓                      
-                          ┃         ┃                      
-              'none'╺━━━━━┫ ABUFFER ┣━━━━━╸'default'       
-          source filter   ┃         ┃        audio         
-                          ┗━━━━━━━━━┛                      
-                                                           
"""
