# 1. Clonando Repositórios
repository_url = input()
git_command = "git clone "
print(f"{git_command}{repository_url}")

# 2. Adicionando Arquivos
files_to_add = input()
git_command = "git add "
print(f"{git_command}{files_to_add}")

# 3. Criando uma Branch
new_branch_name = input()
git_command = "git branch "
print(f"{git_command}{new_branch_name}")

# 4. Alternando de Branch
branch_name = input()
git_command = "git checkout "
print(f"{git_command}{branch_name}")

# 5. Mesclando Branches
branch_to_merge = input()
git_command = "git merge "
print(f"{git_command}{branch_to_merge}")