from poppler.pagerenderer import PageRenderer


def test_can_render():
    assert PageRenderer.can_render() is True


def test_render_page(pdf_page):
    renderer = PageRenderer()
    image = renderer.render_page(pdf_page)

    assert image.height == 792
    assert image.width == 612
