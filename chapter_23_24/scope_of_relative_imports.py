'''
• Relative imports apply to imports within packages only. Keep in mind that
this feature’s module search path change applies only to import statements within
module files used as part of a package—that is, intrapackage imports.

• Relative imports apply to the from statement only. Also remember that this
feature’s new syntax applies only to from statements, not import statements. It’s
detected by the fact that the module name in a from begins with one or more dots
(periods). 
- Module names that contain embedded dots but don’t have a leading dot
are package imports, not relative imports.
'''
