from django.db import models

class EstadoRegistro(models.Model):
    EstRegCod = models.CharField(max_length=1, primary_key=True)
    EstRegNom = models.CharField(max_length=50)

    class Meta:
        db_table = 'ESTADO_REGISTRO'
        managed = False

    def __str__(self):
        return self.EstRegNom

class EstadoCliente(models.Model):
    EstCliCod = models.CharField(max_length=1, primary_key=True)
    EstCliNom = models.CharField(max_length=50)
    EstCliEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='EstCliEstReg')

    class Meta:
        db_table = 'ESTADO_CLIENTE'
        managed = False

    def __str__(self):
        return self.EstCliNom

class TipoCliente(models.Model):
    TipCliCod = models.CharField(max_length=1, primary_key=True)
    TipCliNom = models.CharField(max_length=50)
    TipCliEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='TipCliEstReg')

    class Meta:
        db_table = 'TIPO_CLIENTE'
        managed = False

    def __str__(self):
        return self.TipCliNom

class Cliente(models.Model):
    CliCod = models.IntegerField(primary_key=True)
    CliNom = models.CharField(max_length=60)
    CliTip = models.ForeignKey(TipoCliente, on_delete=models.CASCADE, db_column='CliTip')
    CliFecIng = models.DateField()
    CliFecCes = models.DateField(null=True, blank=True)
    CliEst = models.ForeignKey(EstadoCliente, on_delete=models.CASCADE, db_column='CliEst')
    CliEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='CliEstReg')

    class Meta:
        db_table = 'CLIENTE'
        managed = False

    def __str__(self):
        return self.CliNom

class TipoProyecto(models.Model):
    TipProCod = models.CharField(max_length=1, primary_key=True)
    TipProNom = models.CharField(max_length=50)
    TipProEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='TipProEstReg')

    class Meta:
        db_table = 'TIPO_PROYECTO'
        managed = False

    def __str__(self):
        return self.TipProNom

class EstadoProyecto(models.Model):
    EstProCod = models.CharField(max_length=1, primary_key=True)
    EstProNom = models.CharField(max_length=50)
    EstProEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='EstProEstReg')

    class Meta:
        db_table = 'ESTADO_PROYECTO'
        managed = False

    def __str__(self):
        return self.EstProNom

class Proyecto(models.Model):
    ProCod = models.AutoField(primary_key=True)
    ProCliCod = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='ProCliCod')
    ProTipProCod = models.ForeignKey(TipoProyecto, on_delete=models.CASCADE, db_column='ProTipProCod')
    ProSecPro = models.IntegerField()
    ProFecCon = models.DateField()
    ProFecPac = models.DateField(null=True, blank=True)
    ProFecIni = models.DateField(null=True, blank=True)
    ProFecEnt = models.DateField(null=True, blank=True)
    ProFecCie = models.DateField(null=True, blank=True)
    ProMon = models.DecimalField(max_digits=10, decimal_places=2)
    ProMonRea = models.DecimalField(max_digits=10, decimal_places=2)
    ProMonCos = models.DecimalField(max_digits=10, decimal_places=2)
    ProMonCosRea = models.DecimalField(max_digits=10, decimal_places=2)
    ProMonGas = models.DecimalField(max_digits=10, decimal_places=2)
    ProMonGasRea = models.DecimalField(max_digits=10, decimal_places=2)
    ProMonUti = models.DecimalField(max_digits=10, decimal_places=2)
    ProMonUtiRea = models.DecimalField(max_digits=10, decimal_places=2)
    ProEst = models.ForeignKey(EstadoProyecto, on_delete=models.CASCADE, db_column='ProEst')
    ProEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='ProEstReg')

    class Meta:
        db_table = 'PROYECTO'
        unique_together = ('ProCliCod', 'ProTipProCod', 'ProSecPro')
        managed = False

    def __str__(self):
        return f"Proyecto {self.ProCod}"

class DuracionProyecto(models.Model):
    DurProCod = models.IntegerField(primary_key=True)
    DurProProCod = models.ForeignKey(Proyecto, on_delete=models.CASCADE, db_column='DurProProCod')
    DurProDurEst = models.DecimalField(max_digits=5, decimal_places=2)
    DurProFecCal = models.DateField()
    DurProEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='DurProEstReg')

    class Meta:
        db_table = 'DURACION_PROYECTO'
        managed = False

    def __str__(self):
        return f"Duración {self.DurProCod}"

class EtapasProyecto(models.Model):
    EtaProCod = models.IntegerField(primary_key=True)
    EtaProNom = models.CharField(max_length=255)
    EtaProTieEst = models.DecimalField(max_digits=5, decimal_places=2)
    EtaProEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='EtaProEstReg')

    class Meta:
        db_table = 'ETAPAS_PROYECTO'
        managed = False

    def __str__(self):
        return self.EtaProNom

class CargosPersonal(models.Model):
    CarPerCod = models.IntegerField(primary_key=True)
    CarPerNom = models.CharField(max_length=60)
    CarPerEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='CarPerEstReg')

    class Meta:
        db_table = 'CARGOS_PERSONAL'
        managed = False

    def __str__(self):
        return self.CarPerNom

class Personal(models.Model):
    PerCod = models.IntegerField(primary_key=True)
    PerNom = models.CharField(max_length=60)
    PerCar = models.ForeignKey(CargosPersonal, on_delete=models.CASCADE, db_column='PerCar')
    PerCosHor = models.DecimalField(max_digits=5, decimal_places=2)
    PerFecIng = models.DateField()
    PerEst = models.ForeignKey(EstadoCliente, on_delete=models.CASCADE, db_column='PerEst')
    PerEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='PerEstReg')

    class Meta:
        db_table = 'PERSONAL'
        managed = False

    def __str__(self):
        return self.PerNom

class CargosProyecto(models.Model):
    CarProCod = models.IntegerField(primary_key=True)
    CarProNom = models.CharField(max_length=60)
    CarProEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='CarProEstReg')

    class Meta:
        db_table = 'CARGOS_PROYECTO'
        managed = False

    def __str__(self):
        return self.CarProNom

class PersonalCargosProyecto(models.Model):
    PerCarProCod = models.AutoField(primary_key=True)
    PerCarProPerCod = models.ForeignKey(Personal, on_delete=models.CASCADE, db_column='PerCarProPerCod')
    PerCarProCarProCod = models.ForeignKey(CargosProyecto, on_delete=models.CASCADE, db_column='PerCarProCarProCod')
    PerCarProEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='PerCarProEstReg')

    class Meta:
        db_table = 'PERSONAL_CARGOS_PROYECTO'
        unique_together = ('PerCarProPerCod', 'PerCarProCarProCod')
        managed = False

    def __str__(self):
        return f"{self.PerCarProPerCod} - {self.PerCarProCarProCod}"

class ProyectoPersonalCargosProyecto(models.Model):
    ProPerCarProCod = models.AutoField(primary_key=True)
    ProPerCarProCliCod = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='ProPerCarProCliCod')
    ProPerCarProTipProCod = models.ForeignKey(TipoProyecto, on_delete=models.CASCADE, db_column='ProPerCarProTipProCod')
    ProPerCarProSecPro = models.IntegerField()
    ProPerCarProPerCod = models.ForeignKey(Personal, on_delete=models.CASCADE, db_column='ProPerCarProPerCod')
    ProPerCarProCarProCod = models.ForeignKey(CargosProyecto, on_delete=models.CASCADE, db_column='ProPerCarProCarProCod')
    ProPerCarProEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='ProPerCarProEstReg')

    class Meta:
        db_table = 'PROYECTO_PERSONAL_CARGOS_PROYECTO'
        managed = False

    def __str__(self):
        return f"{self.ProPerCarProCod}"

class ProyectoMovimientos(models.Model):
    ProMovCod = models.AutoField(primary_key=True)
    ProMovCliCod = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='ProMovCliCod')
    ProMovTipProCod = models.ForeignKey(TipoProyecto, on_delete=models.CASCADE, db_column='ProMovTipProCod')
    ProMovSecPro = models.IntegerField()
    ProMovPerCod = models.ForeignKey(Personal, on_delete=models.CASCADE, db_column='ProMovPerCod')
    ProMovCarProCod = models.ForeignKey(CargosProyecto, on_delete=models.CASCADE, db_column='ProMovCarProCod')
    ProMovEtaCod = models.ForeignKey(EtapasProyecto, on_delete=models.CASCADE, db_column='ProMovEtaCod')
    ProMovSecEta = models.IntegerField()
    ProMovActCod = models.IntegerField()
    ProMovFecReg = models.DateField()
    ProMovHorTra = models.DecimalField(max_digits=5, decimal_places=2)
    ProMovMinTra = models.DecimalField(max_digits=5, decimal_places=2)
    ProMovEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='ProMovEstReg')

    class Meta:
        db_table = 'PROYECTO_MOVIMIENTOS'
        managed = False

    def __str__(self):
        return f"Movimiento {self.ProMovCod}"

class PlantillaActividades(models.Model):
    PlaActCod = models.IntegerField(primary_key=True)
    PlaActNom = models.CharField(max_length=255)
    PlaActDes = models.TextField()
    PlaActTipProCod = models.ForeignKey(TipoProyecto, on_delete=models.CASCADE, db_column='PlaActTipProCod')
    PlaActEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='PlaActEstReg')

    class Meta:
        db_table = 'PLANTILLA_ACTIVIDADES'
        managed = False

    def __str__(self):
        return self.PlaActNom

class Actividad(models.Model):
    ActCod = models.IntegerField(primary_key=True)
    ActNom = models.CharField(max_length=255)
    ActDes = models.TextField()
    ActTieEst = models.DecimalField(max_digits=5, decimal_places=2)
    ActEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='ActEstReg')
    ActCodPla = models.ForeignKey(PlantillaActividades, on_delete=models.CASCADE, db_column='ActCodPla')
    ActCodEta = models.ForeignKey(EtapasProyecto, on_delete=models.CASCADE, db_column='ActCodEta')

    class Meta:
        db_table = 'ACTIVIDAD'
        managed = False

    def __str__(self):
        return self.ActNom

class TiemposReales(models.Model):
    TieReaCod = models.IntegerField(primary_key=True)
    TieReaCodAct = models.ForeignKey(Actividad, on_delete=models.CASCADE, db_column='TieReaCodAct')
    TieReaAct = models.DecimalField(max_digits=5, decimal_places=2)
    TieReaComAju = models.TextField()
    TieReaFecReg = models.DateField()
    TieReaEstReg = models.ForeignKey(EstadoRegistro, on_delete=models.CASCADE, db_column='TieReaEstReg')

    class Meta:
        db_table = 'TIEMPOS_REALES'
        managed = False

    def __str__(self):
        return f"Tiempo Real {self.TieReaCod}"
