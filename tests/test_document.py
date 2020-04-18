# poppler-python: python binding to the poppler-cpp pdf lib
# Copyright (C) 2020, Charles Brunet <charles@cbrunet.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from poppler import Permission
from poppler import document
from poppler import version

import pytest

from datetime import datetime, timezone


@pytest.fixture()
def locked_document(data_path):
    return document.load_from_file(data_path / "document.pdf")


def test_load_from_data(data_path):
    file_data = (data_path / "document.pdf").read_bytes()
    pdf_document = document.load_from_data(file_data, "owner", "user")
    assert pdf_document.author == "Charles Brunet"


def test_load_with_path(data_path):
    pdf_document = document.load(data_path / "document.pdf", "owner", "user")
    assert pdf_document.author == "Charles Brunet"


def test_load_with_filename(data_path):
    pdf_document = document.load(str(data_path / "document.pdf"), "owner", "user")
    assert pdf_document.author == "Charles Brunet"


def test_load_with_bytes(data_path):
    data = (data_path / "document.pdf").read_bytes()
    pdf_document = document.load(data, "owner", "user")
    assert pdf_document.author == "Charles Brunet"


def test_load_with_file(data_path):
    with (data_path / "document.pdf").open("rb") as f:
        pdf_document = document.load(f, "owner", "user")
    assert pdf_document.author == "Charles Brunet"


def test_load_with_file_not_bytes(data_path):
    with (data_path / "document.pdf").open("r") as f:
        with pytest.raises(TypeError):
            document.load(f, "owner", "user")


def test_load_with_invalid_type():
    with pytest.raises(TypeError):
        document.load(42)


def test_save(pdf_document, tmp_path):
    copy_document = tmp_path / "copy.pdf"
    pdf_document.author = "Valérie Tremblay"
    assert pdf_document.save(copy_document)

    pdf_copy = document.load(copy_document, "owner", "user")
    assert pdf_copy.author == "Valérie Tremblay"


def test_save_a_copy(pdf_document, tmp_path):
    copy_document = tmp_path / "copy.pdf"
    pdf_document.author = "Valérie Tremblay"
    assert pdf_document.save_a_copy(copy_document)

    pdf_copy = document.load(copy_document, "owner", "user")
    assert pdf_copy.author == "Charles Brunet"


def test_pages(pdf_document):
    assert pdf_document.pages == 3


def test_embedded_file(pdf_document):
    assert pdf_document.embedded_files() == []


def test_get_author(pdf_document):
    assert pdf_document.author == "Charles Brunet"


def test_get_creation_date(pdf_document):
    assert pdf_document.creation_date.astimezone(timezone.utc) == datetime(
        2020, 3, 26, 1, 19, 50, tzinfo=timezone.utc
    )


def test_get_creator(pdf_document):
    assert pdf_document.creator == "Writer"


def test_get_keywords(pdf_document):
    assert pdf_document.keywords == ""


def test_get_modification_date(pdf_document):
    assert pdf_document.modification_date is None


def test_get_pdf_id(pdf_document):
    pdf_id = pdf_document.pdf_id
    assert pdf_id.permanent_id == "c2a52b07e1fd69cc3d4fed8a2ea67ab6"
    assert pdf_id.update_id == "c2a52b07e1fd69cc3d4fed8a2ea67ab6"


def test_get_pdf_version(pdf_document):
    version = pdf_document.pdf_version
    assert version == (1, 5)


def test_get_producer(pdf_document):
    assert pdf_document.producer == "LibreOffice 6.4"


def test_get_subject(pdf_document):
    assert pdf_document.subject == ""


def test_get_title(pdf_document):
    assert pdf_document.title == ""


def test_has_embedded_files(pdf_document):
    assert pdf_document.has_embedded_files() is False
    assert not pdf_document.embedded_files()


def test_has_permission(pdf_document):
    assert pdf_document.has_permission(Permission.print) is True
    assert pdf_document.has_permission(Permission.change) is True
    assert pdf_document.has_permission(Permission.copy) is True
    assert pdf_document.has_permission(Permission.add_notes) is True
    assert pdf_document.has_permission(Permission.fill_forms) is True
    assert pdf_document.has_permission(Permission.accessibility) is True
    assert pdf_document.has_permission(Permission.assemble) is True
    assert pdf_document.has_permission(Permission.print_high_resolution) is True


def test_info_date(pdf_document):
    date = pdf_document.info_date("CreationDate")
    assert date.astimezone(timezone.utc) == datetime(
        2020, 3, 26, 1, 19, 50, tzinfo=timezone.utc
    )


def test_info_key(pdf_document):
    info = pdf_document.info_key("Author")
    assert info == "Charles Brunet"


def test_info_keys(pdf_document):
    keys = pdf_document.info_keys()
    assert keys == ["Author", "Creator", "Producer", "CreationDate"]


def test_is_encrypted(pdf_document):
    assert pdf_document.is_encrypted() is True


def test_is_linearized(pdf_document):
    assert pdf_document.is_linearized() is False


def test_is_locked(pdf_document):
    assert pdf_document.is_locked() is False


def test_metadata(pdf_document):
    meta = pdf_document.metadata
    assert meta == ""


def test_set_author(pdf_document):
    author = "Valérie Tremblay"
    pdf_document.author = author
    assert pdf_document.author == author


def test_set_creation_date(pdf_document):
    d = datetime(1980, 7, 19, 10, 30, 50)
    pdf_document.creation_date = d
    assert pdf_document.creation_date == d


def test_set_empty_creation_date(pdf_document):
    pdf_document.creation_date = None
    assert "CreationDate" not in pdf_document.info_keys()


def test_set_creator(pdf_document):
    creator = "Me"
    pdf_document.creator = creator
    assert pdf_document.creator == creator


def test_set_keywords(pdf_document):
    keywords = "one, two, three"
    pdf_document.keywords = keywords
    assert pdf_document.keywords == keywords


def test_set_modification_date(pdf_document):
    d = datetime(1980, 7, 19, 10, 30, 50)
    pdf_document.modification_date = d
    assert pdf_document.modification_date == d


def test_set_producer(pdf_document):
    producer = "Me"
    pdf_document.producer = producer
    assert pdf_document.producer == producer


def test_set_subject(pdf_document):
    subject = "Me"
    pdf_document.subject = subject
    assert pdf_document.subject == subject


def test_set_title(pdf_document):
    title = "The document title"
    pdf_document.title = title
    assert pdf_document.title == title


def test_set_info_date(pdf_document):
    d = datetime(1980, 7, 19, 10, 30, 50)
    assert pdf_document.set_info_date("CreationDate", d) is True
    assert pdf_document.creation_date == d


def test_set_info_key(pdf_document):
    author = "Valérie Tremblay"
    assert pdf_document.set_info_key("Author", author) is True
    assert pdf_document.author == author


def test_infos(pdf_document):
    infos = pdf_document.infos()
    assert infos["Author"] == "Charles Brunet"


def test_remove_info(pdf_document):
    pdf_document.remove_info()
    assert not pdf_document.infos()


def test_page_layout(pdf_document):
    layout = pdf_document.page_layout
    assert layout == pdf_document.PageLayout.no_layout


def test_page_mode(pdf_document):
    mode = pdf_document.page_mode
    assert mode == pdf_document.PageMode.use_none


def test_locked_document(locked_document):
    assert locked_document.is_locked()


def test_unlock(locked_document):
    result = locked_document.unlock("owner", "user")
    assert result is False
    assert result is locked_document.is_locked()


def test_unlock_with_owner(locked_document):
    result = locked_document.unlock("owner", "")
    assert result is False
    assert result is locked_document.is_locked()


def test_unlock_with_user(locked_document):
    result = locked_document.unlock("", "user")
    assert result is False
    assert result is locked_document.is_locked()


def test_unlock_with_wrong_passwords(locked_document):
    result = locked_document.unlock("abc", "def")
    assert result is True
    assert result is locked_document.is_locked()


@pytest.mark.skipif(version() < (0, 74, 0), reason="Requires at least Poppler 0.74.0")
def test_create_destination_map(pdf_document):
    assert not pdf_document.create_destination_map()


def test_create_toc(pdf_document):
    assert pdf_document.create_toc() is None


@pytest.mark.parametrize("page", range(3))
def test_create_font_iterator(pdf_document, page):
    font_iterator = pdf_document.create_font_iterator(page)

    assert font_iterator.current_page == page


def test_fonts(pdf_document):
    fonts = pdf_document.fonts()

    assert len(fonts) == 1
