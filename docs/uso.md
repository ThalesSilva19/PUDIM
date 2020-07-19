
### Pre requisitos do sistema:

- [python3](https://www.python.org/download/releases/3.0/) 
- [spim](http://spimsimulator.sourceforge.net/) (pode usar outros simuladores de mips, mas a gente usa spim)

### Para instalar utilize:

```bash
sudo apt install python3 && sudo apt install spim 
git fetch https://github.com/ThalesSilva19/mipsPython
```

### Para converter para MIPS 
Vá até o diretório onde você instalou o PUDIM (MipsPython) e digite:
```bash
python3 pudim.py nome_arquivo_entrada nome_arquivo_saida  
```

### Para executar use:

```bash
spim -f nome_arquivo_saida  
```
