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