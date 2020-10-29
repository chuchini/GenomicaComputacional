# Comandos de la Práctica 01
## Jesús Fernando Moreno Ruíz

# Parte I.

**Respuesta 1:** 

```bash
echo $0
bash
```

**Respuesta 2:** 

```bash
mkdir data filtered raw_data meta scripts figures archive
```

**Respuesta 3:**

```bash
mv filtered/ data/ && mv raw_data/ data/
```

**Respuesta 4:**

La organización de directorios es necesario para estructurar y tener un orden de todos los
archivos que conforman algún proyecto bioinformático.

* data: Contiene los datos genéticos utilizados en el proyecto, los datos genéticos pueden dividirse a su vez en subdirectorios como raw, filtered
genotypes, data_in, data_out de modo que los datos crudos estén en un directorio y los modificados por análisis subsecuentes en otros directorios.

* meta, info o docs: Es donde podemos guardar todos los metadatos, como un archivo cvs detallando información de cada una de las muestras. También se puede
guardar cualquier otro documento necesario para procesar los datos.

* bin o scripts: Es la carpeta donde se guarda todos los scripts necesarios para correr el análisis de principio a fin.

* figures: Aquí se puede poner el código que se utilice sólo para hacer las figuras de una publicación dada.

* archive: Es un directorio en donde se guardan scripts que ya no son útiles pero aún se desean conservar por si se llegan a ocupar.

# Parte II.

**Respuesta 1:**
```bash
chmod 777 delay.sh
```

**Respuesta 2:**
```bash
ls -lth
```

**Respuesta 3:**
Agregamos al archivo delay.sh la siguiente línea:
```bash
sleep 30
```

**Respuesta 4:**
```bash
kill -9 <PID>
```

# Parte III.

**Respuesta 1:**
Dentro de la carpeta meta ejecutamos el siguiente comando para crear el archivo indicado:
```bash
touch SarsCvo-2.txt
```

**Respuesta 2:**
Para renombrar cada archivo ejecutamos lo siguiente:
```bash
mv <nombre_archivo_original> <nuevo_nombre_archivo>
```

Para crear el nuevo archivo en la carpeta meta ejecutamos:
```bash
touch SarsCvo-2_Spike.txt
```

Para mover los archivos al directorio `data\raw`
```bash
mv sarscov2_assembly.fasta.gz sarscov2_genome.fasta sarscov2_genome.gff3 splike_a.faa splike_b.faa splike_c.faa SRR10971381_R1.fastq.gz SRR10971381_R2.fastq.gz ../../GenomicaComputacional/jmoreno_p01/data/raw_data/
```

# Parte IV.

**Respuesta 1:**
```bash
ln -s ../raw_data/splike_c.faa && ln -s ../raw_data/splike_b.faa && ln -s ../raw_data/splike_a.faa 
```

**Respuesta 2:**
```bash
touch glycoproteins.faa
```

**Respuesta 3:**
```bash
head -1 splike_a.faa 
>pdb|6VXX|A Chain A, SARS-CoV-2 spike glycoprotein

head -1 splike_b.faa 
>pdb|6VXX|B Chain B, SARS-CoV-2 spike glycoprotein

head -1 splike_c.faa 
>pdb|6VXX|C Chain C, SARS-CoV-2 spike glycoprotein
```

**Respuesta 4:**
```bash
less -n-1 splike* >> glycoproteins.faa 
```

**Respuesta 5:**
```bash
mv splike_*.faa ../../archive/
```
Una vez que movemos los archivos de lugar, las ligas simcólicas se rompen y si tratamos de acceder a ellas en el folder
de `\data\filtered` nos marcara un error de: `No such file or directory`

**Respuesta 6:**
```bash
head -3 sarscov2_genome.fasta && zless sarscov2_assembly.fasta.gz | head -3
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC
>NODE_1_length_264_cov_161.042781
CACAAATCTTAACACTCTTCCCTACACGACGCTCTTCCGATCTACGCCGGGCCATTCGTA
CGAACCGATACCTGTGGTAAAGGGTCCTACTGTATGGTGGTACACGAGTAGTAGCAAATG
```

**Respuesta 7:**
```bash
grep '>' sarscov2_genome.fasta | wc -l && zless sarscov2_assembly.fasta.gz | grep '>' | wc -l
1
35
```

**Respuesta 8:**
Utilizando lo que sabemos de los archivos .fastq (lo explicamos más a fondo en la siguiente pregunta) sabemos
que la línea donde se encuentra la secuencia es donde puede haber un patrón como `AAA`, por lo tanto es posible
utilizar para encontrar las secuencias. Sin embargo pienso que esto puede fallar para archivos más grandes, siendo
mejor utilizar AWK para encontrar los codones de inicio y fin para delimitar una secuencia.
```bash
zless SRR10971381_R2.fastq.gz | head -12 | uniq -c | grep 'AAA' -c
3
```

**Respuesta 9:**
los archivos .faa y .fasta hacen referencia a lo mismo (pueden ser nucleótidos o aminoácidos) mientras que .fastqc también
hace referencia a lo mismo pero tiene el siguiente formato:
1. Una línea que empieza con `@`, conteniendo el ID de la secuencia.
2. Una o más líneas que contienen la secuencia.
3. Una nueva línea que empieza con el caracter `+`, y empieza en blanco o reptiendo el ID de la secuencia.
4. Una o más líneas que contienen el puntaje de calidad.
Siendo esta última la característica diferente. Un registro FASTQ contiene una secuencia de puntuaciones de calidad para cada nucleótido.

**Respuesta 10:**
La diferencia radica en la forma en que la información es desplegada, es decir, `less sequence.gff3` nos muestra un archivo desordenado del cual
es difícil entender su estructura original, mientras que usando `less -S sequence.gff3` nos encontramos con una mejor estructura visible, siendo
que podemos notar que no hay salto de líneas que interrumpan el texto, sino que la pantalla abarca todo el contenido, línea por línea, siendo que
para movernos entre la información hay que movernos entre derecha e izquierda para leer toda la información. Lo despliega en columnas.

**Respuesta 11:**
```bash
cut -f3 sarscov2_genome.gff3 | grep 'gene' -c
11
```
El campo 3 nos muestra información de si es gene o CDS, entre otras más.
COn base a la documentación encontré que se describe el algoritmo o el 
procedimiento que generó esta característica. Normalmente, Genescane o Genebank, respectivamente.