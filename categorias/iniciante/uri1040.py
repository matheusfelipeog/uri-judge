# -*- coding: utf-8 -*-


def aprova_nova_media(n_media):
    if n_media >= 5.0:
        print('Aluno aprovado.')
    elif n_media <= 4.9:
        print('Aluno reprovado.')

    return 'Media final: {:.1f}'.format(n_media)


n1, n2, n3, n4 = map(float, input().split())

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')

elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')

    nota_exame = float(input())
    print('Nota do exame: {:.1f}'.format(nota_exame))

    print(aprova_nova_media((media + nota_exame) / 2))

elif media < 5.0:
    print('Aluno reprovado.')
