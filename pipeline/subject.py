'''
Schema of subject information.
'''
import datajoint as dj
from . import reference

schema = dj.schema(dj.config.get('database.prefix', '') + 'subject')


@schema
class Species(dj.Lookup):
    definition = """
    species: varchar(24)
    """
    contents = zip(['Mus musculus'])


@schema
class Strain(dj.Lookup): 
    definition = """ 
    strain: varchar(24)
    """
    contents = zip(['C57BL6', 'Ai35D', 'VGAT-ChR2-EYFP', 'Ai32', 'GAD2-Cre', 'PV-Cre', 'N/A'])
  
    
@schema
class StrainAlias(dj.Lookup):
    definition = """  # Other animal strain names that may be used interchangeably in different studies
    strain_alias: varchar(128)
    ---
    -> Strain
    """
    contents = [
            ['C57BL6', 'C57BL6'],
            ['C57Bl/6', 'C57BL6'],
            ['Ai35D', 'Ai35D'],
            ['Ai32', 'Ai32'],
            ['129S-Gt(ROSA)26Sortm32(CAG-COP4*H134R/EYFP)Hze/J', 'Ai32'],
            ['GAD2_Cre', 'GAD2-Cre'],
            ['GAD2-Cre', 'GAD2-Cre'],
            ['Gad2-IRES-Cre', 'GAD2-Cre'],
            ['PV-IRES-Cre', 'PV-Cre'],
            ['129P2-Pvalbtm1(cre)Arbr/J', 'PV-Cre'],
            ['VGAT-ChR2-EYFP', 'VGAT-ChR2-EYFP'],
            ['VGAT-ChR2(H134R)-EYFP', 'VGAT-ChR2-EYFP'],
            ['N/A', 'N/A']
            ]


@schema
class Subject(dj.Manual):  # temporarily remove species, strain and animalsource
    definition = """
    subject_id: varchar(64)  # id of the subject (e.g. ANM244028)
    ---
    -> Species
    -> reference.AnimalSource
    sex = 'U': enum('M', 'F', 'U')
    date_of_birth = NULL: date
    subject_description=null:   varchar(1024) 
    """

    class Strain(dj.Part):
        definition = """
        -> master
        -> Strain
        """