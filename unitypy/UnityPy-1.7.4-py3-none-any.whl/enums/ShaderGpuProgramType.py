from enum import IntEnum


class ShaderGpuProgramType(IntEnum):
    kShaderGpuProgramUnknown = 0
    kShaderGpuProgramGLLegacy = 1
    kShaderGpuProgramGLES31AEP = 2
    kShaderGpuProgramGLES31 = 3
    kShaderGpuProgramGLES3 = 4
    kShaderGpuProgramGLES = 5
    kShaderGpuProgramGLCore32 = 6
    kShaderGpuProgramGLCore41 = 7
    kShaderGpuProgramGLCore43 = 8
    kShaderGpuProgramDX9VertexSM20 = 9
    kShaderGpuProgramDX9VertexSM30 = 10
    kShaderGpuProgramDX9PixelSM20 = 11
    kShaderGpuProgramDX9PixelSM30 = 12
    kShaderGpuProgramDX10Level9Vertex = 13
    kShaderGpuProgramDX10Level9Pixel = 14
    kShaderGpuProgramDX11VertexSM40 = 15
    kShaderGpuProgramDX11VertexSM50 = 16
    kShaderGpuProgramDX11PixelSM40 = 17
    kShaderGpuProgramDX11PixelSM50 = 18
    kShaderGpuProgramDX11GeometrySM40 = 19
    kShaderGpuProgramDX11GeometrySM50 = 20
    kShaderGpuProgramDX11HullSM50 = 21
    kShaderGpuProgramDX11DomainSM50 = 22
    kShaderGpuProgramMetalVS = 23
    kShaderGpuProgramMetalFS = 24
    kShaderGpuProgramSPIRV = 25
    kShaderGpuProgramConsoleVS = 26
    kShaderGpuProgramConsoleFS = 27
    kShaderGpuProgramConsoleHS = 28
    kShaderGpuProgramConsoleDS = 29
    kShaderGpuProgramConsoleGS = 30
    kShaderGpuProgramRayTracing = 31
