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
from functools import singledispatch, wraps
from pathlib import Path


PDFId = namedtuple("PDFId", ["permanent_id", "update_id"])


class LockedDocumentError(RuntimeError):
    def __init__(self):
        super().__init__("Cannot perform this operation on a locked document.")


def ensure_unlocked(fct):
    @wraps(fct)
    def wrapper(self, *args, **kwargs):
        if self._document.is_locked():
            raise LockedDocumentError()
        return fct(self, *args, **kwargs)

    return wrapper


class Document:

    PageLayout = document.page_layout_enum
    PageMode = document.page_mode_enum

    def __init__(self, poppler_document, data=None):
        self._document = poppler_document
        self._data = data

    @ensure_unlocked
    def create_font_iterator(self, page=0):
        return FontIterator(self._document.create_font_iterator(page))

    @ensure_unlocked
    def create_toc(self):
        t = self._document.create_toc()
        return Toc(t) if t else None

    @ensure_unlocked
    def create_page(self, index):
        return Page(self._document.create_page(index))

    @property
    @ensure_unlocked
    def author(self):
        return self.info_key("Author")

    @author.setter
    @since(0, 46)
    @ensure_unlocked
    def author(self, author):
        self.set_info_key("Author", author)

    @property
    @ensure_unlocked
    def creation_date(self):
        return self.info_date("CreationDate")

    @creation_date.setter
    @since(0, 46)
    @ensure_unlocked
    def creation_date(self, creation_date):
        self.set_info_date("CreationDate", creation_date)

    @property
    @ensure_unlocked
    def creator(self):
        return self.info_key("Creator")

    @creator.setter
    @since(0, 46)
    @ensure_unlocked
    def creator(self, creator):
        self.set_info_key("Creator", creator)

    @property
    @ensure_unlocked
    def keywords(self):
        return self.info_key("Keywords")

    @keywords.setter
    @since(0, 46)
    @ensure_unlocked
    def keywords(self, keywords):
        self.set_info_key("Keywords", keywords)

    @property
    @ensure_unlocked
    def metadata(self):
        meta = self._document.metadata()
        return str(meta)

    @property
    @ensure_unlocked
    def modification_date(self):
        return self.info_date("ModDate")

    @modification_date.setter
    @since(0, 46)
    @ensure_unlocked
    def modification_date(self, modification_date):
        self.set_info_date("ModDate", modification_date)

    @property
    def pdf_id(self):
        return PDFId(*self._document.get_pdf_id())

    @property
    def pdf_version(self):
        return self._document.get_pdf_version()

    @property
    @ensure_unlocked
    def producer(self):
        return self.info_key("Producer")

    @producer.setter
    @since(0, 46)
    @ensure_unlocked
    def producer(self, producer):
        self.set_info_key("Producer", producer)

    @property
    @ensure_unlocked
    def subject(self):
        return self.info_key("Subject")

    @subject.setter
    @since(0, 46)
    @ensure_unlocked
    def subject(self, subject):
        self.set_info_key("Subject", subject)

    @property
    @ensure_unlocked
    def title(self):
        return self.info_key("Title")

    @title.setter
    @since(0, 46)
    @ensure_unlocked
    def title(self, title):
        self.set_info_key("Title", title)

    @property
    @ensure_unlocked
    def pages(self):
        return self._document.pages()

    @since(0, 74)
    @ensure_unlocked
    def create_destination_map(self):
        return {
            name: Destination(destination)
            for name, destination in self._document.create_destination_map().items()
        }

    @ensure_unlocked
    def embedded_files(self):
        return [EmbeddedFile(f) for f in self._document.embedded_files()]

    @ensure_unlocked
    def fonts(self):
        return [FontInfo(i) for i in self._document.fonts()]

    @ensure_unlocked
    def has_embedded_files(self):
        return self._document.has_embedded_files()

    def has_permission(self, which):
        return self._document.has_permission(which)

    @ensure_unlocked
    def info_date(self, key):
        timestamp = self._document.info_date(key)
        return from_time_type(timestamp)

    @since(0, 46)
    @ensure_unlocked
    def set_info_date(self, key, val):
        return self._document.set_info_date(key, to_time_type(val))

    @ensure_unlocked
    def info_key(self, key):
        info = self._document.info_key(key)
        return str(info)

    @ensure_unlocked
    def infos(self):
        """Get the document info dictionary as a dict object."""
        info_dict = {}
        for key in self._document.info_keys():
            if key.endswith("Date"):
                info_dict[key] = self.info_date(key)
            else:
                info_dict[key] = self.info_key(key)
        return info_dict

    @since(0, 46)
    @ensure_unlocked
    def set_info_key(self, key, val):
        return self._document.set_info_key(key, ustring(val))

    @ensure_unlocked
    def info_keys(self):
        return self._document.info_keys()

    def is_encrypted(self):
        return self._document.is_encrypted()

    def is_linearized(self):
        return self._document.is_linearized()

    def is_locked(self):
        return self._document.is_locked()

    @property
    @ensure_unlocked
    def page_layout(self):
        return self._document.page_layout()

    @property
    @ensure_unlocked
    def page_mode(self):
        return self._document.page_mode()

    @since(0, 46)
    @ensure_unlocked
    def remove_info(self):
        return self._document.remove_info()

    @since(0, 46)
    @ensure_unlocked
    def save(self, file_name):
        return self._document.save(str(file_name))

    @since(0, 46)
    @ensure_unlocked
    def save_a_copy(self, file_name):
        return self._document.save_a_copy(str(file_name))

    def unlock(self, owner_password, user_password):
        return self._document.unlock(owner_password, user_password)


def load_from_file(file_name, owner_password=None, user_password=None):
    return Document(
        document.load_from_file(
            str(file_name), owner_password or "", user_password or ""
        )
    )


def load_from_data(file_data: bytes, owner_password=None, user_password=None):
    return Document(
        document.load_from_data(file_data, owner_password or "", user_password or ""),
        file_data
    )


@singledispatch
def load(arg, owner_password=None, user_password=None):
    try:
        data = arg.read()
        return load_from_data(data, owner_password, user_password)

    except AttributeError:
        raise TypeError(
            "Load cannot be called with argument of type {}".format(type(arg))
        )

    except UnicodeDecodeError:
        raise TypeError("Stream must be read as bytes.")


@load.register(str)
def _(arg: str, owner_password=None, user_password=None):
    return load_from_file(arg, owner_password, user_password)


@load.register(Path)
def _(arg: Path, owner_password=None, user_password=None):
    return load_from_file(arg, owner_password, user_password)


@load.register(bytes)
def _(arg: bytes, owner_password=None, user_password=None):
    return load_from_data(arg, owner_password, user_password)
