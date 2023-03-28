import shutil
import os

# Run at MultiMC/instances/
# Remember to change GTNH folder name below
old_folder = os.path.join(os.getcwd(), "GT_New_Horizons_2.2.3_(MMC)", ".minecraft")
new_folder = os.path.join(os.getcwd(), "GT_New_Horizons_2.3.2_Java_8", ".minecraft")

# Installing and Migrating - GTNH wiki page
## Cleaning destination folder before copying old files (if needed)
# shutil.rmtree(os.path.join(new_folder, "saves"))
# shutil.rmtree(os.path.join(new_folder, "journeymap"))
# shutil.rmtree(os.path.join(new_folder, "visualprospecting"))
# shutil.rmtree(os.path.join(new_folder, "TCNodeTracker"))
# shutil.rmtree(os.path.join(new_folder, "shaderpacks"))
# shutil.rmtree(os.path.join(new_folder, "screenshots"))
# shutil.rmtree(os.path.join(new_folder, "backups"))

## Saves
shutil.copytree( os.path.join(old_folder, "saves")
               , os.path.join(new_folder, "saves"))

shutil.copytree( os.path.join(old_folder, "journeymap")
               , os.path.join(new_folder, "journeymap"))

shutil.copytree( os.path.join(old_folder, "visualprospecting")
               , os.path.join(new_folder, "visualprospecting"))

shutil.copytree( os.path.join(old_folder, "TCNodeTracker")
               , os.path.join(new_folder, "TCNodeTracker"))

## Shaderpacks
shutil.copytree( os.path.join(old_folder, "shaderpacks")
               , os.path.join(new_folder, "shaderpacks"))

## Screenshots
#shutil.copytree( os.path.join(old_folder, "screenshots")
#               , os.path.join(new_folder, "screenshots"))

## Backups
#shutil.copytree( os.path.join(old_folder, "backups")
#               , os.path.join(new_folder, "backups"))

## Game options
shutil.copy( os.path.join(old_folder, "options.txt")
           , os.path.join(new_folder, "options.txt"))

shutil.copy( os.path.join(old_folder, "optionsof.txt")
           , os.path.join(new_folder, "optionsof.txt"))

shutil.copy( os.path.join(old_folder, "optionsshaders.txt")
           , os.path.join(new_folder, "optionsshaders.txt"))

# Custom Rules
## Disable mods
dir_path = os.path.join(new_folder, "mods")
disabled_keywords = ["fairplay", "defaultworldgenerator"]

for filename in os.listdir(dir_path):
    if any(keyword in filename for keyword in disabled_keywords):
        # Construct the new file name
        new_filename = filename + ".disabled"
        
        # Rename the file
        os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))

## Custom mods
dir_path = os.path.join(old_folder, "mods")
custom_keywords = ["ClimateControl", "RTG", "OptiFine", "unlimited"]
for filename in os.listdir(dir_path):
    if any(keyword in filename for keyword in custom_keywords):
        source_path = os.path.join(dir_path, filename)
        destination_path = os.path.join(new_folder, "mods", filename)

        shutil.copy(source_path, destination_path)

## Disable Pollution
with open(os.path.join(old_folder, "config", "GregTech", "GregTech.cfg"), "r+") as file:
    # Read all lines of the file
    lines = file.readlines()
    
    # Look for lines containing the keyword to replace
    for i, line in enumerate(lines):
        if "B:EnablePollution" in line:
            # Replace the line with the new line
            lines[i] = "    B:EnablePollution=false"
    
    # Write the modified lines back to the file
    file.seek(0)
    file.writelines(lines)
    file.truncate()

## Gamerules
### mobGriefing: False
### keepInventory: True
### doMobSpawning: False
