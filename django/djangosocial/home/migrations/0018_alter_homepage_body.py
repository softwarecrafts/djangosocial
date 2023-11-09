# Generated by Django 4.2.6 on 2023-11-09 16:46

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_footer_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock()), ('hero_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('gallery', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Choose an image.', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='An optional caption for the image.', required=False))])))])), ('timeline', wagtail.blocks.StructBlock([('timeline_moments', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock()), ('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock())])))])), ('stats', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('stats', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('number', wagtail.blocks.CharBlock()), ('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock()), ('size', wagtail.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]))]), max_num=3))])), ('hero', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('content_list', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list_title', wagtail.blocks.CharBlock()), ('list_type', wagtail.blocks.CharBlock(help_text='What does the list of represent? (eg roles, events)')), ('content_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('link', wagtail.blocks.PageChooserBlock())]), max_num=3)), ('more_list_text', wagtail.blocks.CharBlock()), ('more_list_link', wagtail.blocks.PageChooserBlock())])), ('content_with_images', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('secondary_paragraph', wagtail.blocks.TextBlock()), ('top_image', wagtail.images.blocks.ImageChooserBlock()), ('bottom_left_image', wagtail.images.blocks.ImageChooserBlock()), ('bottom_center_image', wagtail.images.blocks.ImageChooserBlock()), ('bottom_right_image', wagtail.images.blocks.ImageChooserBlock())])), ('logo_cloud', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('logos', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))], null=True, use_json_field=True),
        ),
    ]
