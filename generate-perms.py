#!/usr/bin/env python3

# Format Example:

format = """Bypass Form:
Perm Group Name: cheesebypass
Steam64 ID: 76561198185423987
Item Bypasses (Separated by ,): 58176, 58177
Vehicle Bypasses (Separated by ,): 13640, 13641"""

# This script is used to generate the XML for a role in RocketMod's Permissions.config.xml file.

mode = "bypass"

if mode == "bypass":
  #format = str(input("Enter Bypass Format: "))
  lst = []
  format = format.strip().split("\n")
  for item in format:
    lst.append(item.split(":")[1].strip())
  id = lst[1].lower()
  display_name = id
  colour = "ffffff"
  member = lst[2]

  with open("output.xml", "w") as f:
    f.write("    <Group>\n")
    f.write(f"      <Id>{id}</Id>\n")
    f.write(f"      <DisplayName>{display_name}</DisplayName>\n")
    f.write("      <Prefix />\n")
    f.write("      <Suffix />\n")
    f.write(f"      <Color>#{colour}</Color>\n")
    f.write("      <Members>\n")
    f.write(f"        <Member>{member}</Member>\n")
    f.write("      </Members>\n")
    f.write("      <ParentGroup>default</ParentGroup>\n")
    f.write("      <Priority>100</Priority>\n")
    f.write("      <Permissions>\n")
    for item in lst[3].split(","):
      f.write(f'        <Permission Cooldown="0">bypass.{item.lstrip()}</Permission>\n')
    for item in lst[4].split(","):
      f.write(f'        <Permission Cooldown="0">vehiclebypass.{item.lstrip()}</Permission>\n')
    f.write("      </Permissions>\n")
    f.write("    </Group>")
    print("Done!")