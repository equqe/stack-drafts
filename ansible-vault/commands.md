создание секретного файла хранилища, содержащего ключ шифрования, который шифрует переменные:

```
touch .vault_pass.txt
echo 'YOUR_CONFIG_PASS' > .vault_pass.txt
```

чтобы зашифровать переменные:

```
ansible-vault encrypt group_vars/vars.yml --vault-password-file .vault_pass.txt
```

чтобы расшифровать переменные:

```
ansible-vault decrypt group_vars/vars.yml --vault-password-file .vault_pass.txt
```