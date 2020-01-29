import os

os.chdir('<DIR>/fastq/')
#print(os.getcwd())

FILENAME = []

for name in os.listdir():
    if name.split('.')[-1] == str('fastq'):
        FILENAME.append(name.split('.')[0])

ServerConnect ='\n#!/bin/bash\n#PBS -l nodes={nodes}:ppn={ppn}\n#PBS -l walltime={walltime}\n#PBS -l gres=ccm\n#PBS -o {outlog}\n#PBS -e {errlog}\n#PBS -N {name}\n'
Module ='\nmodule load ccmrun\nmodule load hisat\nmodule load samtools\nmodule load stringtie\n\n' 

#             
        
class NGS_pipeline:
    def __init__(self):
            self.C1 = []
            self.C2 = []
            self.C3 = []
            self.C4 = []
    def fq2sam(self, c1):
        for i in FILENAME:
            c1 = str('hisat -x -p -q ')+i + str('.fastq -o ')+i+str('.sam')
            self.C1.append(c1)
    def sam2bam(self,c2):
        for i in FILENAME:
            c2 = str('samtools -view -bS ')+i + str('.sam -o ')+i+str('.bam')
            self.C2.append(c2)
    def bam2sortedbam(self,c3):
        for i in FILENAME:
            c3 = str('samtools -view -bS ')+i + str('.bam -o ')+i+str('.sorted')
            self.C3.append(c3)
    def sortedbam2gtf(self,c4):
        for i in FILENAME:
            c4 = str('stringtie ')+i + str('.sorted.bam -o ')+i+str('.gtf')
            self.C4.append(c4)

#NOTE: Command should be changed as per the user defined parameters
##Below call can be switched On or Off, as per user choice
        
Mycode = NGS_pipeline()
Mycode.fq2sam('')
Mycode.sam2bam('')
Mycode.bam2sortedbam('')
Mycode.sortedbam2gtf('')

for z in FILENAME:
#    print(str(FILENAME.index(z))+ '\t'+ z)
    with open (str(z)+str('.sh'),"w") as f:
        f.write(ServerConnect)
        f.write(Module)
        for i in Mycode.C1, Mycode.C2, Mycode.C3, Mycode.C4:
            print (i[FILENAME.index(z)], file=f)
#Run on linux => for f in $(find -name '*.sh'); do qsub $f; done

