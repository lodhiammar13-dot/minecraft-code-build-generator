print("=== Minecraft Build Generator (Java Edition) ===")

length = int(input("Enter length (blocks): "))
width = int(input("Enter width (blocks): "))
height = int(input("Enter height (blocks): "))

block = input("Enter block name (e.g. stone, oak_planks, quartz_block): ").lower()

mode = input("Solid or hollow? (solid/hollow): ").lower()

x = length - 1
y = height - 1
z = width - 1

if mode == "hollow":
    command = f"/fill ~ ~ ~ ~{x} ~{y} ~{z} minecraft:{block} hollow"
else:
    command = f"/fill ~ ~ ~ ~{x} ~{y} ~{z} minecraft:{block}"

print("\n✅ Copy this command into Minecraft:")
print(command)
