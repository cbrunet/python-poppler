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

from poppler.cpp import document
from poppler.cpp.global_ import ustring
from poppler.utilities import from_time_type, to_time_type
from poppler.destination import Destination
from poppler.embeddedfile import EmbeddedFile
from poppler.font import FontInfo, FontIterator
from poppler.page import Page
from poppler.toc import Toc
from poppler.utilities import since

from collections import namedtuple
from functools import singledispatch
from pathlib import Path


PDFId = namedtuple("PDFId", ["permanent_id", "update_id"])


class Document:

    PageLayout = document.page_layout_enum
    PageMode = document.page_mode_enum

    def __init__(self, poppler_document):
        self._document = poppler_document

    def create_font_iterator(self, page=0):
        return FontIterator(self._document.create_font_iterator(page))

    def create_toc(self):
        t = self._document.create_toc()
        return Toc(t) if t else None

    def create_page(self, index):
        return Page(self._document.create_page(index))

    @property
    def author(self):
        return str(self._document.get_author())

    @author.setter
    def author(self, author):
        self._document.set_author(ustring(author))

    @property
    def creation_date(self):
        timestamp = self._document.get_creation_date()
        return from_time_type(timestamp)

    @creation_date.setter
    def creation_date(self, creation_date):
        self._document.set_creation_date(to_time_type(creation_date))

    @property
    def creator(self):
        return str(self._document.get_creator())

    @creator.setter
    def creator(self, creator):
        self._document.set_creator(ustring(creator))

    @property
    def keywords(self):
        return str(self._document.get_keywords())

    @keywords.setter
    def keywords(self, keywords):
        self._document.set_keywords(ustring(keywords))

    @property
    def metadata(self):
        meta = self._document.metadata()
        return str(meta)

    @property
    def modification_date(self):
        timestamp = self._document.get_modification_date()
        return from_time_type(timestamp)

    @modification_date.setter
    def modification_date(self, modification_date):
        self._document.set_modification_date(to_time_type(modification_date))

    @property
    def pdf_id(self):
        return PDFId(*self._document.get_pdf_id())

    @property
    def pdf_version(self):
        return self._document.get_pdf_version()

    @property
    def producer(self):
        return str(self._document.get_producer())

    @producer.setter
    def producer(self, producer):
        self._document.set_producer(ustring(producer))

    @property
    def subject(self):
        return str(self._document.get_subject())

    @subject.setter
    def subject(self, subject):
        self._document.set_subject(ustring(subject))

    @property
    def title(self):
        return str(self._document.get_title())

    @title.setter
    def title(self, title):
        self._document.set_title(ustring(title))

    @property
    def pages(self):
        return self._document.pages()

    @since(0, 74)
    def create_destination_map(self):
        return {
            name: Destination(destination)
            for name, destination in self._document.create_destination_map().items()
        }

    def embedded_files(self):
        return [EmbeddedFile(f) for f in self._document.embedded_files()]

    def fonts(self):
        return [FontInfo(i) for i in self._document.fonts()]

    def has_embedded_files(self):
        return self._document.has_embedded_files()

    def has_permission(self, which):
        return self._document.has_permission(which)

    def info_date(self, key):
        timestamp = self._document.info_date(key)
        return from_time_type(timestamp)

    def set_info_date(self, key, val):
        return self._document.set_info_date(key, to_time_type(val))

    def info_key(self, key):
        info = self._document.info_key(key)
        return str(info)

    def infos(self):
        """Get the document info dictionary as a dict object."""
        info_dict = {}
        for key in self._document.info_keys():
            if key.endswith("Date"):
                info_dict[key] = self.info_date(key)
            else:
                info_dict[key] = self.info_key(key)
        return info_dict

    def set_info_key(self, key, val):
        return self._document.set_info_key(key, ustring(val))

    def info_keys(self):
        return self._document.info_keys()

    def is_encrypted(self):
        return self._document.is_encrypted()

    def is_linearized(self):
        return self._document.is_linearized()

    def is_locked(self):
        return self._document.is_locked()

    @property
    def page_layout(self):
        return self._document.page_layout()

    @property
    def page_mode(self):
        return self._document.page_mode()

    def remove_info(self):
        return self._document.remove_info()

    def save(self, file_name):
        return self._document.save(str(file_name))

    def save_a_copy(self, file_name):
        return self._document.save_a_copy(str(file_name))

    def unlock(self, owner_password, user_password):
        return self._document.unlock(owner_password, user_password)


def load_from_file(file_name, owner_password="", user_password=""):
    return Document(
        document.load_from_file(str(file_name), owner_password, user_password)
    )


def load_from_data(file_data: bytes, owner_password="", user_password=""):
    return Document(document.load_from_data(file_data, owner_password, user_password))


@singledispatch
def load(arg, owner_password="", user_password=""):
    try:
        data = arg.read()
        return load_from_data(data, owner_password, user_password)

    except AttributeError:
        raise TypeError(
            "Load cannot be called with argument of type {}".format(type(arg))
        )

    except UnicodeDecodeError:
        raise TypeError("Stream must be read as bytes.")


@load.register
def _(arg: str, owner_password="", user_password=""):
    return load_from_file(arg, owner_password, user_password)


@load.register
def _(arg: Path, owner_password="", user_password=""):
    return load_from_file(arg, owner_password, user_password)


@load.register
def _(arg: bytes, owner_password="", user_password=""):
    return load_from_data(arg, owner_password, user_password)
