import pysam


# Use pysam to filter BAM to a specified CHR
class DownselectBAM:
    def __init__(self, bam_path, chr):
        self.bam_path = bam_path
        self.chr = chr

        self.bam = pysam.AlignmentFile(self.bam_path, "rb")

    # Output a downselected BAM only containing reads of specified CHR
    def downselect(self):
        # Get the filename
        filename = self.bam_path.split("/")[-1] if "/" in self.bam_path else self.bam_path
        out_filename = "CHR" + self.chr + "_" + filename
        self.downselected_bam = pysam.AlignmentFile(out_filename, "wb", template=self.bam)

        print("Beginning downselection...")
        for read in self.bam.fetch(self.chr):
            self.downselected_bam.write(read)

        self.downselected_bam.close()
        self.bam.close()
        print("Done!")
