from fontmake.font_project import FontProject
from fontTools.varLib import build

# Roman

romans = [
	"Roman/Amstelvar-Roman.ufo",
#	"Roman/Amstelvar-opszmax.ufo",
]

project = FontProject()
project.run_from_ufos(
	romans, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "Amstelvar-Roman.designspace"
outfile = "../fonts/Amstelvar-Roman-VF.ttf"
finder = lambda s: s.replace("Roman/", "master_ttf_interpolatable/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print "Saving Variable Font..."
varfont.save(outfile)
print "DONE!"

# Italic

italics = [
	"Italic/Amstelvar-Italic.ufo",
#	"Italic/Amstelvar-ital-opszmax.ufo",
]

project = FontProject()
project.run_from_ufos(
	italics, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "Amstelvar-Italic.designspace"
outfile = "../fonts/Amstelvar-Italic-VF.ttf"
finder = lambda s: s.replace("Italic/", "master_ttf_interpolatable/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print "Saving Variable Font..."
varfont.save(outfile)
print "DONE!"
