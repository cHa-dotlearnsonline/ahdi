# Generated by Django 4.2.7 on 2023-12-19 21:22

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "intro",
                    wagtail.fields.RichTextField(
                        blank=True, help_text="Describe what images are in this gallery"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StandardIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("introduction", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.AddField(
            model_name="homepage",
            name="featured_section_1",
            field=models.ForeignKey(
                blank=True,
                help_text="Will display 3 child elements.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Featured section 1",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="featured_section_1_title",
            field=models.CharField(
                blank=True,
                help_text="Title to show above the promo copy",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="featured_section_2",
            field=models.ForeignKey(
                blank=True,
                help_text="Will display 3 child elements.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Featured section 2",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="featured_section_2_title",
            field=models.CharField(
                blank=True,
                help_text="Title to show above the promo copy",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="featured_section_3",
            field=models.ForeignKey(
                blank=True,
                help_text="Will display 3 child elements.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Featured section 3",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="featured_section_3_title",
            field=models.CharField(
                blank=True,
                help_text="Title to show above the promo copy",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="goal_text",
            field=wagtail.fields.RichTextField(
                blank=True,
                help_text="Write some text to describe your organisation's Goals",
                max_length=500,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="goal_title",
            field=models.CharField(
                blank=True, help_text="Title for organisation Goals", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_cta",
            field=models.CharField(
                blank=True,
                help_text="Text to display for main page button",
                max_length=255,
                verbose_name="Hero Call to Action",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_cta_link",
            field=models.CharField(
                blank=True,
                help_text="make a link to a page either internal or external that directs to  where vistor should go",
                max_length=1000,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Homepage image 1",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_image_1",
            field=models.ForeignKey(
                blank=True,
                help_text="Homepage image 1",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_image_text",
            field=wagtail.fields.RichTextField(
                blank=True,
                help_text="In less than 500 characters describe something to be displayed on top of this image",
                max_length=500,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_image_text_1",
            field=wagtail.fields.RichTextField(
                blank=True,
                help_text="In less than 500 characters describe something to be displayed on top of this image",
                max_length=500,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_image_title",
            field=models.CharField(
                blank=True,
                help_text="Huge title to display for above image",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_image_title_1",
            field=models.CharField(
                blank=True,
                help_text="Huge title to display for above image",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="mission_text",
            field=wagtail.fields.RichTextField(
                blank=True,
                help_text="Write some text to describe your organisation's mission",
                max_length=500,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="mission_title",
            field=models.CharField(
                blank=True, help_text="Title for organisation mission", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="promo_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Put the promtional image here",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="promo_text",
            field=wagtail.fields.RichTextField(
                blank=True,
                help_text="Add some descriptive context for this image",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="promo_title",
            field=models.CharField(
                blank=True, help_text="The promotion title", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="vision_text",
            field=wagtail.fields.RichTextField(
                blank=True,
                help_text="Write some text to describe your organisation's vision",
                max_length=500,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="vision_title",
            field=models.CharField(
                blank=True, help_text="Title for company Vision", max_length=255
            ),
        ),
        migrations.CreateModel(
            name="StandardPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "introduction",
                    models.TextField(
                        blank=True, help_text="Text to describe what's on the page"
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.blocks.CharBlock(form_clasname="title"),
                            ),
                            ("paragraph", wagtail.blocks.RichTextBlock()),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                            ("URL", wagtail.blocks.URLBlock()),
                            ("blockquote", wagtail.blocks.BlockQuoteBlock()),
                            ("embedlink", wagtail.embeds.blocks.EmbedBlock()),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Page body",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Place a landscape image here",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="DisplayImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "introduction",
                    models.TextField(
                        blank=True, help_text="Text to describe the image"
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Upload top quality images of high quality",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photo",
                        to="home.gallerypage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
