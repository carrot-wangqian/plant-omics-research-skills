"""Combine the six separately maintained content specs for the visuals."""
from reading_explainer import DATA as READING
from preflight_analysis import DATA as PREFLIGHT
from figure_writing import DATA as WRITING
DATA={**READING,**PREFLIGHT,**WRITING}
