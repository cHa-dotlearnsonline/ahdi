from django.db import models
from wagtail.models import Page, Collection, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey


class HomePage(Page):
    #this will be where i write the code for the homepage 
    #Copy the image feature from bakerydemo
    #hero section will have up to 2 images only
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete= models.SET_NULL,
        related_name= "+",
        help_text= "Homepage image 1"
    )

    hero_image_title = models.CharField(
        blank=True, max_length = 255, help_text="Huge title to display for above image"
    )
    hero_image_text = RichTextField(
        null=True, blank=True, max_length= 500, help_text="In less than 500 characters describe something to be displayed on top of this image"
    )

    hero_image_1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete= models.SET_NULL,
        related_name= "+",
        help_text= "Homepage image 1"
    )

    hero_image_title_1 = models.CharField(
        blank=True, max_length = 255, help_text="Huge title to display for above image"
    )
    hero_image_text_1 = RichTextField(
        null=True, blank=True, max_length= 500, help_text="In less than 500 characters describe something to be displayed on top of this image"
    )

    hero_cta = models.CharField(
        verbose_name="Hero Call to Action",
        blank=True,
        max_length=255,
        help_text="Text to display for main page button"
    )

    hero_cta_link = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        help_text = "make a link to a page either internal or external that directs to  where vistor should go",
    )
    #TODO: The Promo Section
    promo_title = models.CharField(blank=True, max_length=255, help_text="The promotion title")
    promo_image= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Put the promtional image here"
    )
    promo_text = RichTextField(
        null=True, blank=True, help_text="Add some descriptive context for this image"
    )
    #TODO: Goals and motivations Sections
    vision_title= models.CharField(blank=True, max_length=255, help_text="Title for company Vision")
    vision_text = RichTextField(blank=True, max_length=500, help_text="Write some text to describe your organisation's vision")
    vision_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="an Image to represent your vision"
    )
    mission_title= models.CharField(blank=True, max_length=255, help_text="Title for organisation mission")
    mission_text = RichTextField(blank=True, max_length=500, help_text="Write some text to describe your organisation's mission")
    mission_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="an Image to represent your vision"
    )
    goal_title= models.CharField(blank=True, max_length=255, help_text="Title for organisation Goals")
    goal_text = RichTextField(blank=True, max_length=500, help_text="Write some text to describe your organisation's Goals")
    goal_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="an Image to represent your vision"
    )
    ## create featured content fields for featured sections
    featured_section_1_title = models.CharField(
        blank=True, max_length=255, help_text="Title to show above the promo copy"
    )

    featured_section_1 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Will display 3 child elements.",
        verbose_name = "Featured section 1"
    )

    featured_section_2_title = models.CharField(
        blank=True, max_length=255, help_text="Title to show above the promo copy"
    )

    featured_section_2 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Will display 3 child elements.",
        verbose_name = "Featured section 2"
    )

    featured_section_3_title = models.CharField(
        blank=True, max_length=255, help_text="Title to show above the promo copy"
    )

    featured_section_3 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Will display 3 child elements.",
        verbose_name = "Featured section 3"
    )

    partners = StreamField(
        [
         ('Partner_infor', blocks.StructBlock([
             ('partner_logo', ImageChooserBlock(required=False)),
             ('partner_URL', blocks.URLBlock()),
         ])),
         ],
        verbose_name="Patners", blank = True, use_json_field=True
    )

    #TODO: complete and update the content panels to reflect new design
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("hero_cta"),
                        FieldPanel("hero_cta_link")

                    ]

                ),
                MultiFieldPanel(
                    [
                        FieldPanel("hero_image_title"),
                        FieldPanel("hero_image"),
                        FieldPanel("hero_image_text"),
                    ]
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("hero_image_1"),
                        FieldPanel("hero_image_title_1"),
                        FieldPanel("hero_image_text_1"),
                    ]
                )

            ],
            heading="The hero section"
        ),
        MultiFieldPanel(
            [  
            MultiFieldPanel(
                [
                    FieldPanel("vision_title"),
                    FieldPanel("vision_text")
                ]
            ),
             MultiFieldPanel(
                [
                    FieldPanel("mission_title"),
                    FieldPanel("mission_text")
                ]
            ),
             MultiFieldPanel(
                [
                    FieldPanel("goal_title"),
                    FieldPanel("goal_text")
                ]
            ),

            ],
            heading="Stragetic Plan statements i.e goals, mission and vision"
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                    FieldPanel("promo_title"),
                    FieldPanel("promo_image"),
                    FieldPanel("promo_text")
                    ]

                )
               
            ],
            heading="Promotional Content"
        ),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("featured_section_1_title"),
                        FieldPanel("featured_section_1")
                    ]
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("featured_section_2_title"),
                        FieldPanel("featured_section_2")
                    ]
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("featured_section_3_title"),
                        FieldPanel("featured_section_3")
                    ]
                ),

            ],
            heading="Featured Homepage Sections"
        ),
        FieldPanel("partners")
    ]

class GalleryPage(Page):
    #this will have an inline panel to add more images
    """The Gallery Page is a page that just displays images"""
    intro = RichTextField(help_text="Describe what images are in this gallery", blank=True)
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete= models.SET_NULL,
        related_name="+",
        help_text="Upload a good quality image to Represent this gallery"
    )
    content_panels = Page.content_panels + [
        InlinePanel('photo', label="Gallery Images")
    ] 


class DisplayImage(Orderable):
    """This will be the standard way to put images in collections and then 
    display them to the users. I have copied much of the code from the Bakery Demo"""
    page= ParentalKey(GalleryPage, on_delete=models.CASCADE, related_name="photo")
    introduction = models.TextField(help_text="Text to describe the image", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+", 
        help_text="Upload top quality images of high quality"   
    )
    panels = [
        FieldPanel("introduction"),
        FieldPanel("image"),
    ]


class StandardPage(Page):

    """This will display a standard page that has an image, a title, an introduction and some rich text"""
    introduction= models.TextField(help_text="Text to describe what's on the page", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Place a landscape image here"
    )
    body = StreamField(
        [('heading', blocks.CharBlock(form_clasname="title")),
         ('paragraph', blocks.RichTextBlock()),
         ('image', ImageChooserBlock()),
         ('URL', blocks.URLBlock()),
         ('blockquote', blocks.BlockQuoteBlock()),
         ('embedlink', EmbedBlock())],
        verbose_name="Page body", blank = True, use_json_field=True
    )
    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("introduction"),
        FieldPanel("image"),
        FieldPanel("body"),
    ]

class StandardIndexPage(Page):
    introduction= RichTextField(blank=True)
    def get_context(self, request):
        context = super().get_context(request)
        stories=self.get_children().live().order_by('-first_published_at')
        context['stories'] = stories
        return context
    content_panels = Page.content_panels + [
        FieldPanel('introduction')
    ]

class GalleryIndexPage(Page):
    """This is being created so that I can take advantage of the gallery page 
    that i have created. This is so that on this one page I can display all the
    Galleries the organisation will have"""
    introduction = RichTextField(blank=True, help_text="Write some text to describe this page. This page is meant to host Gallery Page type subpages")
    def get_context(self, request):
        context = super().get_context(request)
        galleries = self.get_children().live()
        context["galleries"] = galleries
        return context
    content_panels = Page.content_panels + [
        FieldPanel("introduction")
    ]