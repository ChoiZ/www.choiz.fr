Ajout dans mon .vimrc de matchadd() & highlight
###############################################
:date: 2012-04-27 15:11:26
:author: choiz
:category: text
:tags: vimrc, vim, config file, .vimrc, todo, notice, fixme, highlight, matchadd
:slug: 2012-04-27-ajout-dans-mon-vimrc-de-matchadd-highlight
:status: published

Petit ajout dans mon fichier .vimrc ::

    " Highlight To do list with green background
    highlight Todo ctermfg=black ctermbg=green guifg=black guibg=green
    highlight Notice ctermfg=white ctermbg=blue guifg=white guibg=blue
    highlight Fixme ctermfg=white ctermbg=red guifg=white guibg=red
    " Match todolist, notice, fixme
    :call matchadd('Todo','[T|t][O|o][D|d][O|o]')
    :call matchadd('Todo','[T|t][O|o] [D|d][O|o]')
    :call matchadd('Notice','[N|n][O|o][T|t][I|i][C|c][E|e]')
    :call matchadd('Notice','[N|n][O|o][T|t][E|e]')
    :call matchadd('Fixme','[F|f][I|i][X|x][M|m][E|e]')
    :call matchadd('Fixme','[F|f][I|i][X|x] [M|m][E|e]')

