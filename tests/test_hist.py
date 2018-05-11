#!/usr/bin/env python

# Copyright (c) 2017, DIANA-HEP
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest

import numpy

from histbook.axis import *
from histbook.hist import *

class TestHist(unittest.TestCase):
    def runTest(self):
        pass

    def test_calc(self):
        h = Hist(bin("x + 0.1", 10, 0, 1))
        h.fill(x=numpy.array([0.4, 0.3, 0.3, 0.5, 0.4, 0.8]))
        self.assertEqual(h._content.tolist(), [[0], [0], [0], [0], [0], [2], [2], [1], [0], [0], [1], [0], [0]])

    def test_bin(self):
        h = Hist(bin("x", 10, 10, 11))
        h.fill(x=numpy.array([10.4, 10.3, 10.3, 10.5, 10.4, 10.8]))
        self.assertEqual(h._content.tolist(), [[0], [0], [0], [0], [2], [2], [1], [0], [0], [1], [0], [0], [0]])

        h = Hist(bin("x", 10, 0, 1))
        h.fill(x=numpy.array([0.4, 0.3, 123, 99, 0.3, numpy.nan, numpy.nan, numpy.nan, 0.5, -99, 0.4, 0.8]))
        self.assertEqual(h._content.tolist(), [[1], [0], [0], [0], [2], [2], [1], [0], [0], [1], [0], [2], [3]])

        h = Hist(bin("x", 10, 0, 1, underflow=False))
        h.fill(x=numpy.array([0.4, 0.3, 123, 99, 0.3, numpy.nan, numpy.nan, numpy.nan, 0.5, -99, 0.4, 0.8]))
        self.assertEqual(h._content.tolist(), [[0], [0], [0], [2], [2], [1], [0], [0], [1], [0], [2], [3]])

        h = Hist(bin("x", 10, 0, 1, overflow=False))
        h.fill(x=numpy.array([0.4, 0.3, 123, 99, 0.3, numpy.nan, numpy.nan, numpy.nan, 0.5, -99, 0.4, 0.8]))
        self.assertEqual(h._content.tolist(), [[1], [0], [0], [0], [2], [2], [1], [0], [0], [1], [0], [3]])

        h = Hist(bin("x", 10, 0, 1, nanflow=False))
        h.fill(x=numpy.array([0.4, 0.3, 123, 99, 0.3, numpy.nan, numpy.nan, numpy.nan, 0.5, -99, 0.4, 0.8]))
        self.assertEqual(h._content.tolist(), [[1], [0], [0], [0], [2], [2], [1], [0], [0], [1], [0], [2]])

        h = Hist(bin("x", 10, 0, 1, underflow=False, overflow=False, nanflow=False))
        h.fill(x=numpy.array([0.4, 0.3, 123, 99, 0.3, numpy.nan, numpy.nan, numpy.nan, 0.5, -99, 0.4, 0.8]))
        self.assertEqual(h._content.tolist(), [[0], [0], [0], [2], [2], [1], [0], [0], [1], [0]])

        h = Hist(bin("x", 2, 0, 2))
        h.fill(x=numpy.array([0.0, 0.0001, 0.0001, 0.5, 0.5, 0.5, 0.9999, 0.9999, 0.9999, 0.9999, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0001, 1.0001, 1.0001, 1.0001, 1.0001, 1.0001, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.9999, 1.9999, 1.9999, 1.9999, 1.9999, 1.9999, 1.9999, 1.9999, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001]))
        self.assertEqual(h._content.tolist(), [[0], [1 + 2 + 3 + 4], [5 + 6 + 7 + 8], [9 + 10], [0]])

        h = Hist(bin("x", 2, 0, 2, closedlow=False))
        h.fill(x=numpy.array([0.0, 0.0001, 0.0001, 0.5, 0.5, 0.5, 0.9999, 0.9999, 0.9999, 0.9999, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0001, 1.0001, 1.0001, 1.0001, 1.0001, 1.0001, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.9999, 1.9999, 1.9999, 1.9999, 1.9999, 1.9999, 1.9999, 1.9999, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001, 2.0001]))
        self.assertEqual(h._content.tolist(), [[1], [2 + 3 + 4 + 5], [6 + 7 + 8 + 9], [10], [0]])

    def test_binbin(self):
        print("")
        h = Hist(bin("x", 3, 0, 3, underflow=False, overflow=False, nanflow=False), bin("y", 5, 0, 5, underflow=False, overflow=False, nanflow=False))
        h.fill(x=numpy.array([1]), y=numpy.array([3]))
        self.assertEqual(h._content.tolist(), [[[0], [0], [0], [0], [0]], [[0], [0], [0], [1], [0]], [[0], [0], [0], [0], [0]]])