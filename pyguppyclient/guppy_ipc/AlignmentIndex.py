# automatically generated by the FlatBuffers compiler, do not modify

# namespace: guppy_ipc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AlignmentIndex(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAlignmentIndex(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AlignmentIndex()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def AlignmentIndexBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x30\x30\x30\x32", size_prefixed=size_prefixed)

    # AlignmentIndex
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AlignmentIndex
    def IndexName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AlignmentIndex
    def Header(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def AlignmentIndexStart(builder): builder.StartObject(2)
def AlignmentIndexAddIndexName(builder, indexName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(indexName), 0)
def AlignmentIndexAddHeader(builder, header): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(header), 0)
def AlignmentIndexEnd(builder): return builder.EndObject()