# Generated by Django 5.2 on 2025-05-25 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnalysisFileType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=45)),
                ("abbrev", models.CharField(max_length=10)),
                ("variant", models.IntegerField(default=0)),
                (
                    "description",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnalysisOutputType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=45, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="AnalysisType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=50, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Barcode",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Bardex",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
                ("seqtext", models.CharField(max_length=100)),
                ("note", models.CharField(blank=True, max_length=255, null=True)),
                ("rc_seqtext", models.CharField(max_length=100)),
                ("abbrev_label", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="DownstreamAnalysisType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=45)),
                ("abbrev", models.CharField(max_length=10)),
                ("description", models.CharField(max_length=4096)),
                ("active", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Gemstone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="InstrumentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="LibraryType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Organism",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Pool",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
                (
                    "description",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
                ("date_created", models.DateField(blank=True, null=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Protocol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=2048, null=True),
                ),
                ("is_current", models.IntegerField(default=1)),
                ("adapter_length", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SampleType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SequenceType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=45)),
                ("abbrev", models.CharField(max_length=20)),
                ("active", models.BooleanField(default=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SpecimenSource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Flowcell",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("label", models.CharField(max_length=100)),
                ("employee_id", models.IntegerField(blank=True, null=True)),
                ("date_created", models.DateField(blank=True, null=True)),
                ("clustering_station_id", models.IntegerField(blank=True, null=True)),
                (
                    "old_comments",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                ("is_paired_end", models.BooleanField(blank=True, null=True)),
                ("failed", models.BooleanField(blank=True, null=True)),
                ("active", models.BooleanField(blank=True, null=True)),
                (
                    "barcode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="flowcells",
                        to="core.barcode",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Analyses",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("date_performed", models.DateField(blank=True, null=True)),
                ("notes", models.CharField(blank=True, max_length=2048, null=True)),
                (
                    "software_version",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("contaminant_filtered", models.BooleanField(blank=True, null=True)),
                (
                    "analysis_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="analyses",
                        to="core.analysistype",
                    ),
                ),
                (
                    "flowcell",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="analyses",
                        to="core.flowcell",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Instrument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
                (
                    "instrument_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="instruments",
                        to="core.instrumenttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lane",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField()),
                ("is_control", models.BooleanField(blank=True, null=True)),
                ("is_titer", models.BooleanField(blank=True, null=True)),
                ("failed", models.BooleanField(blank=True, null=True)),
                (
                    "flowcell",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lanes",
                        to="core.flowcell",
                    ),
                ),
                (
                    "pool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lanes",
                        to="core.pool",
                    ),
                ),
                (
                    "sequence_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.sequencetype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Library",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
                ("employee_id", models.IntegerField(blank=True, null=True)),
                ("date_created", models.DateField(blank=True, null=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=4096, null=True),
                ),
                ("insert_size", models.IntegerField(blank=True, null=True)),
                ("client_provided", models.BooleanField(blank=True, null=True)),
                ("active", models.BooleanField(blank=True, null=True)),
                (
                    "bardex",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="library_index_1",
                        to="core.bardex",
                    ),
                ),
                (
                    "second_bardex",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="library_index_2",
                        to="core.bardex",
                    ),
                ),
                (
                    "library_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.librarytype",
                    ),
                ),
                (
                    "protocol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.protocol"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LibraryLane",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("units", models.CharField(max_length=10)),
                ("concentration", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "lane",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="library_lanes",
                        to="core.lane",
                    ),
                ),
                (
                    "library",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="library_lanes",
                        to="core.library",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
                ("ftp_url", models.CharField(blank=True, max_length=50, null=True)),
                ("ftp_user", models.CharField(blank=True, max_length=10, null=True)),
                ("website_url", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "website_user",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
                (
                    "website_password",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "old_comments",
                    models.TextField(blank=True, max_length=4096, null=True),
                ),
                ("is_current", models.BooleanField(default=False)),
                ("active", models.BooleanField(default=True)),
                (
                    "gemstone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="core.gemstone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReferenceGenome",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=255)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "organism",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reference_genomes",
                        to="core.organism",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CoordinateSet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=255)),
                (
                    "source_file",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "reference_genome",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="coordinate_sets",
                        to="core.referencegenome",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Run",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("label", models.CharField(max_length=100)),
                ("date_started", models.DateField(blank=True, null=True)),
                ("date_completed", models.DateField(blank=True, null=True)),
                ("cycles", models.IntegerField(blank=True, null=True)),
                ("employee_id", models.IntegerField(blank=True, null=True)),
                ("notes", models.CharField(blank=True, max_length=2048, null=True)),
                ("cycle1_attachment_id", models.IntegerField(blank=True, null=True)),
                (
                    "read2_cycle1_attachment_id",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "flowcell",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="runs",
                        to="core.flowcell",
                    ),
                ),
                (
                    "instrument",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="runs",
                        to="core.instrument",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sample",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=4096, null=True),
                ),
                (
                    "organism",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="samples",
                        to="core.organism",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="samples",
                        to="core.project",
                    ),
                ),
                (
                    "sample_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.sampletype",
                    ),
                ),
                (
                    "specimen_source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.specimensource",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="library",
            name="sample",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="libraries",
                to="core.sample",
            ),
        ),
        migrations.CreateModel(
            name="DownstreamAnalysis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=50)),
                ("analysis_date", models.DateTimeField(blank=True, null=True)),
                ("base_dir", models.CharField(blank=True, max_length=1024, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
                (
                    "coordinate_set",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="downstream_analyses",
                        to="core.coordinateset",
                    ),
                ),
                (
                    "downstream_analysis_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="downstream_analyses",
                        to="core.downstreamanalysistype",
                    ),
                ),
                (
                    "reference_genome",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="downstream_analyses",
                        to="core.referencegenome",
                    ),
                ),
                (
                    "sample",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="downstream_analyses",
                        to="core.sample",
                    ),
                ),
                (
                    "sequence_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="downstream_analyses",
                        to="core.sequencetype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnalysisOutput",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_primary", models.BooleanField(default=False)),
                (
                    "analysis_output_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.analysisoutputtype",
                    ),
                ),
                (
                    "analysis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="outputs",
                        to="core.downstreamanalysis",
                    ),
                ),
                (
                    "sample",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="analysis_outputs",
                        to="core.sample",
                    ),
                ),
                (
                    "sequence_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="analysis_outputs",
                        to="core.sequencetype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnalysisOutputTypeDownstreamFileType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "analysis_file_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="analysis_output_types",
                        to="core.analysisfiletype",
                    ),
                ),
                (
                    "analysis_output_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="downstream_file_types",
                        to="core.analysisoutputtype",
                    ),
                ),
            ],
            options={
                "unique_together": {("analysis_output_type", "analysis_file_type")},
            },
        ),
        migrations.CreateModel(
            name="DownstreamAnalysisFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file_path", models.CharField(max_length=750)),
                ("include_freq", models.IntegerField(default=0)),
                (
                    "description",
                    models.CharField(blank=True, max_length=2048, null=True),
                ),
                (
                    "downstream_analysis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="downstream_analysis_files",
                        to="core.downstreamanalysis",
                    ),
                ),
                (
                    "downstream_analysis_file_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="downstream_analysis_files",
                        to="core.analysisfiletype",
                    ),
                ),
            ],
            options={
                "unique_together": {("file_path", "downstream_analysis")},
            },
        ),
        migrations.CreateModel(
            name="ProtocolHasBardex",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bardex",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="protocol_has_bardexes",
                        to="core.bardex",
                    ),
                ),
                (
                    "protocol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="protocol_has_bardexes",
                        to="core.protocol",
                    ),
                ),
            ],
            options={
                "unique_together": {("protocol", "bardex")},
            },
        ),
    ]
