from base64 import b64decode
import hashlib
import logging

from django.test import TestCase

from django_bootstrap5.core import get_bootstrap_setting
import urllib.request



class UrlValidityTestCase(TestCase):
    def test_get_bootstrap_setting(self):
        """ Tests that it's possible to pull the URLs listed in the settings, and the hashes match.
        """

        logger = logging.getLogger(__name__)

        jsurl = get_bootstrap_setting("javascript_url")
        cssurl = get_bootstrap_setting("css_url")

        for link in (jsurl, cssurl):
            req = urllib.request.Request(url=link.get("url"), method='GET')

            hashtype, hash = link.get("integrity").split("-")
            hash_decoded = b64decode(hash)
            self.assertTrue(hasattr(hashlib, hashtype))

            with urllib.request.urlopen(req) as request:
                logger.debug(f"Status for {link.get('url')}: {request.status}")
                # test that we're getting a "valid" response code from the specified URL
                self.assertLess(request.status,400)

                # Test that the integrity hash matches
                hasher = hashlib.new(hashtype)
                hasher.update(request.read())
                self.assertEqual(hasher.digest(), hash_decoded)

