#!/usr/bin/env python3

mode = "bypass"
item_bypass = ["58176", "58177"]
vehicle_bypass = ["13640", "13640"]
if mode == "bypass":
  id = str(input("Enter Role ID: ")).lower()
  display_name = id
  colour = str(input("Enter Role Colour: ")).lower().lstrip("#")
  member = str(input("Enter Player's Steam ID: "))

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
    f.write("      <Priority>30</Priority>\n")
    f.write("      <Permissions>\n")
    for item in item_bypass:
      f.write(f'        <Permission Cooldown="0">bypass.{item}</Permission>\n')
    for item in vehicle_bypass:
      f.write(f'        <Permission Cooldown="0">vehiclebypass.{item}</Permission>\n')
    f.write("      </Permissions>\n")
    f.write("    </Group>")
    print("Done!")