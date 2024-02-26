from .utils import *
from dataclasses import dataclass, field as dataclasses_field
from typing import Literal

AVCODECCONTEXT_FLAGS = Literal['unaligned', 'mv4', 'qpel', 'loop', 'gray', 'psnr', 'ildct', 'low_delay', 'global_header', 'bitexact', 'aic', 'ilme', 'cgop', 'output_corrupt', 'drop_changed']
AVCODECCONTEXT_FLAGS2 = Literal['fast', 'noout', 'ignorecrop', 'local_header', 'chunks', 'showall', 'export_mvs', 'skip_manual', 'ass_ro_flush_noop', 'icc_profiles']
AVCODECCONTEXT_EXPORT_SIDE_DATA = Literal['mvs', 'prft', 'venc_params', 'film_grain']
AVCODECCONTEXT_BUG = Literal['autodetect', 'xvid_ilace', 'ump4', 'no_padding', 'amv', 'qpel_chroma', 'std_qpel', 'qpel_chroma2', 'direct_blocksize', 'edge', 'hpel_chroma', 'dc_clip', 'ms', 'trunc', 'iedge']
AVCODECCONTEXT_STRICT = Literal['very', 'strict', 'normal', 'unofficial', 'experimental']
AVCODECCONTEXT_ERR_DETECT = Literal['crccheck', 'bitstream', 'buffer', 'explode', 'ignore_err', 'careful', 'compliant', 'aggressive']
AVCODECCONTEXT_DCT = Literal['auto', 'fastint', 'int', 'mmx', 'altivec', 'faan']
AVCODECCONTEXT_IDCT = Literal['auto', 'int', 'simple', 'simplemmx', 'arm', 'altivec', 'simplearm', 'simplearmv5te', 'simplearmv6', 'simpleneon', 'xvid', 'xvidmmx', 'faani', 'simpleauto']
AVCODECCONTEXT_EC = Literal['guess_mvs', 'deblock', 'favor_inter']
AVCODECCONTEXT_DEBUG = Literal['pict', 'rc', 'bitstream', 'mb_type', 'qp', 'dct_coeff', 'green_metadata', 'skip', 'startcode', 'er', 'mmco', 'bugs', 'buffers', 'thread_ops', 'nomc']
AVCODECCONTEXT_MBD = Literal['simple', 'bits', 'rd']
AVCODECCONTEXT_THREADS = Literal['auto']
AVCODECCONTEXT_PROFILE = Literal['unknown', 'main10']
AVCODECCONTEXT_LEVEL = Literal['unknown']
AVCODECCONTEXT_CMP = Literal['sad', 'sse', 'satd', 'dct', 'psnr', 'bit', 'rd', 'zero', 'vsad', 'vsse', 'nsse', 'w53', 'w97', 'dctmax', 'chroma', 'msad']
AVCODECCONTEXT_SKIP_LOOP_FILTER = Literal['none', 'default', 'noref', 'bidir', 'nokey', 'nointra', 'all']
AVCODECCONTEXT_COLOR_PRIMARIES = Literal['bt709', 'unknown', 'bt470m', 'bt470bg', 'smpte170m', 'smpte240m', 'film', 'bt2020', 'smpte428', 'smpte428_1', 'smpte431', 'smpte432', 'jedec-p22', 'ebu3213', 'unspecified']
AVCODECCONTEXT_COLOR_TRC = Literal['bt709', 'unknown', 'gamma22', 'gamma28', 'smpte170m', 'smpte240m', 'linear', 'log100', 'log316', 'iec61966-2-4', 'bt1361e', 'iec61966-2-1', 'bt2020-10', 'bt2020-12', 'smpte2084', 'smpte428', 'arib-std-b67', 'unspecified', 'log', 'log_sqrt', 'iec61966_2_4', 'bt1361', 'iec61966_2_1', 'bt2020_10bit', 'bt2020_12bit', 'smpte428_1']
AVCODECCONTEXT_COLORSPACE = Literal['rgb', 'bt709', 'unknown', 'fcc', 'bt470bg', 'smpte170m', 'smpte240m', 'ycgco', 'bt2020nc', 'bt2020c', 'smpte2085', 'chroma-derived-nc', 'chroma-derived-c', 'ictcp', 'unspecified', 'ycocg', 'bt2020_ncl', 'bt2020_cl']
AVCODECCONTEXT_COLOR_RANGE = Literal['unknown', 'tv', 'pc', 'unspecified', 'mpeg', 'jpeg']
AVCODECCONTEXT_CHROMA_SAMPLE_LOCATION = Literal['unknown', 'left', 'center', 'topleft', 'top', 'bottomleft', 'bottom', 'unspecified']
AVCODECCONTEXT_THREAD_TYPE = Literal['slice', 'frame']
AVCODECCONTEXT_AUDIO_SERVICE_TYPE = Literal['ma', 'ef', 'vi', 'hi', 'di', 'co', 'em', 'vo', 'ka']
AVCODECCONTEXT_SUB_CHARENC_MODE = Literal['do_nothing', 'auto', 'pre_decoder', 'ignore']
AVCODECCONTEXT_FIELD_ORDER = Literal['progressive', 'tt', 'bb', 'tb', 'bt']
AVCODECCONTEXT_HWACCEL_FLAGS = Literal['ignore_level', 'allow_high_depth', 'allow_profile_mismatch', 'unsafe_output']

@dataclass
class AVCodecContext(): # AVCodecContext
 b:int = 200000
 ab:int = 128000
 bt:int = 4000000
 flags:AVCODECCONTEXT_FLAGS = '0'
 flags2:AVCODECCONTEXT_FLAGS2 = '0'
 export_side_data:AVCODECCONTEXT_EXPORT_SIDE_DATA = '0'
 g:int = 12
 ar:int = 0
 ac:int = 0
 cutoff:int = 0
 frame_size:int = 0
 qcomp:float = '0.5'
 qblur:float = '0.5'
 qmin:int = 2
 qmax:int = 31
 qdiff:int = 3
 bf:int = 0
 b_qfactor:float = '1.25'
 bug:AVCODECCONTEXT_BUG = 'autodetect'
 strict:AVCODECCONTEXT_STRICT = 'normal'
 b_qoffset:float = '1.25'
 err_detect:AVCODECCONTEXT_ERR_DETECT = '0'
 maxrate:int = 0
 minrate:int = 0
 bufsize:int = 0
 i_qfactor:float = '-0.8'
 i_qoffset:float = '0'
 dct:AVCODECCONTEXT_DCT = 'auto'
 lumi_mask:float = '0'
 tcplx_mask:float = '0'
 scplx_mask:float = '0'
 p_mask:float = '0'
 dark_mask:float = '0'
 idct:AVCODECCONTEXT_IDCT = 'auto'
 ec:AVCODECCONTEXT_EC = 'guess_mvs+deblock'
 aspect:float|str = '0/1'
 sar:float|str = '0/1'
 debug:AVCODECCONTEXT_DEBUG = '0'
 dia_size:int = 0
 last_pred:int = 0
 pre_dia_size:int = 0
 subq:int = 8
 me_range:int = 0
 global_quality:int = 0
 mbd:AVCODECCONTEXT_MBD = 'simple'
 rc_init_occupancy:int = 0
 threads:AVCODECCONTEXT_THREADS = '1'
 dc:int = 0
 nssew:int = 8
 skip_top:int = 0
 skip_bottom:int = 0
 profile:AVCODECCONTEXT_PROFILE = 'unknown'
 level:AVCODECCONTEXT_LEVEL = 'unknown'
 lowres:int = 0
 cmp:AVCODECCONTEXT_CMP = 'sad'
 subcmp:AVCODECCONTEXT_CMP = 'sad'
 mbcmp:AVCODECCONTEXT_CMP = 'sad'
 ildctcmp:AVCODECCONTEXT_CMP = 'vsad'
 precmp:AVCODECCONTEXT_CMP = 'sad'
 mblmin:int = 236
 mblmax:int = 3658
 skip_loop_filter:AVCODECCONTEXT_SKIP_LOOP_FILTER = 'default'
 skip_idct:AVCODECCONTEXT_SKIP_LOOP_FILTER = 'default'
 skip_frame:AVCODECCONTEXT_SKIP_LOOP_FILTER = 'default'
 bidir_refine:int = 1
 keyint_min:int = 25
 refs:int = 1
 trellis:int = 0
 mv0_threshold:int = 256
 compression_level:int = -1
 ch_layout:CHANNEL_LAYOUTS = None
 channel_layout:CHANNEL_LAYOUTS = '0x0'
 request_channel_layout:CHANNEL_LAYOUTS = '0x0'
 rc_max_vbv_use:float = '0'
 rc_min_vbv_use:float = '3'
 ticks_per_frame:int = 1
 color_primaries:AVCODECCONTEXT_COLOR_PRIMARIES = 'unknown'
 color_trc:AVCODECCONTEXT_COLOR_TRC = 'unknown'
 colorspace:AVCODECCONTEXT_COLORSPACE = 'unknown'
 color_range:AVCODECCONTEXT_COLOR_RANGE = 'unknown'
 chroma_sample_location:AVCODECCONTEXT_CHROMA_SAMPLE_LOCATION = 'unknown'
 slices:int = 0
 thread_type:AVCODECCONTEXT_THREAD_TYPE = 'slice+frame'
 audio_service_type:AVCODECCONTEXT_AUDIO_SERVICE_TYPE = 'ma'
 request_sample_fmt:SAMPLE_RMT = 'none'
 sub_charenc:str = None
 sub_charenc_mode:AVCODECCONTEXT_SUB_CHARENC_MODE = '0'
 apply_cropping:bool = True
 skip_alpha:bool = False
 field_order:AVCODECCONTEXT_FIELD_ORDER = '0'
 dump_separator:str = None
 codec_whitelist:str = None
 max_pixels:int = 'INT_MAX'
 max_samples:int = 'INT_MAX'
 hwaccel_flags:AVCODECCONTEXT_HWACCEL_FLAGS = 'ignore_level'
 extra_hw_frames:int = -1
 discard_damaged_percentage:int = 95 
 ...


AMV_ENCODER_MPV_FLAGS = Literal['skip_rd', 'strict_gop', 'qp_rd', 'cbp_rd', 'naq', 'mv0']
AMV_ENCODER_SKIP_CMP = Literal['sad', 'sse', 'satd', 'dct', 'psnr', 'bit', 'rd', 'zero', 'vsad', 'vsse', 'nsse', 'dct264', 'dctmax', 'chroma', 'msad']
AMV_ENCODER_HUFFMAN = Literal['default', 'optimal']

@dataclass
class amv_encoder(): # amv encoder
 mpv_flags:AMV_ENCODER_MPV_FLAGS = '0'
 luma_elim_threshold:int = 0
 chroma_elim_threshold:int = 0
 quantizer_noise_shaping:int = 0
 error_rate:int = 0
 qsquish:float = '0'
 rc_qmod_amp:float = '0'
 rc_qmod_freq:int = 0
 rc_eq:str = None
 rc_init_cplx:float = '0'
 rc_buf_aggressivity:float = '1'
 border_mask:float = '0'
 lmin:int = 236
 lmax:int = 3658
 skip_threshold:int = 0
 skip_factor:int = 0
 skip_exp:int = 0
 skip_cmp:AMV_ENCODER_SKIP_CMP = 'dctmax'
 sc_threshold:int = 0
 noise_reduction:int = 0
 ps:int = 0
 huffman:AMV_ENCODER_HUFFMAN = 'optimal'
 force_duplicated_matrix:bool = False 
 ...


_A_PNG_ENCODER_PRED = Literal['none', 'sub', 'up', 'avg', 'paeth', 'mixed']

@dataclass
class _A_PNG_encoder(): # (A)PNG encoder
 dpi:int = 0
 dpm:int = 0
 pred:_A_PNG_ENCODER_PRED = 'none' 
 ...


CFHD_QUALITY = Literal['film3+', 'film3', 'film2+', 'film2', 'film1.5', 'film1+', 'film1', 'high+', 'high', 'medium+', 'medium', 'low+', 'low']

@dataclass
class cfhd(): # cfhd
 quality:CFHD_QUALITY = 'film3+' 
 ...




@dataclass
class cinepak(): # cinepak
 max_extra_cb_iterations:int = 2
 skip_empty_cb:bool = False
 max_strips:int = 3
 min_strips:int = 1
 strip_number_adaptivity:int = 0 
 ...




@dataclass
class cljr_encoder(): # cljr encoder
 dither_type:int = 1 
 ...


DNXHD_PROFILE = Literal['dnxhd', 'dnxhr_444', 'dnxhr_hqx', 'dnxhr_hq', 'dnxhr_sq', 'dnxhr_lb']

@dataclass
class dnxhd(): # dnxhd
 nitris_compat:bool = False
 ibias:int = 0
 profile:DNXHD_PROFILE = 'dnxhd' 
 ...




@dataclass
class dvvideo_encoder(): # dvvideo encoder
 quant_deadzone:int = 7 
 ...


EXR_COMPRESSION = Literal['none', 'rle', 'zip1', 'zip16']
EXR_FORMAT = Literal['half', 'float']

@dataclass
class exr(): # exr
 compression:EXR_COMPRESSION = 'none'
 format:EXR_FORMAT = 'float'
 gamma:float = '1' 
 ...


FFV1_ENCODER_CODER = Literal['rice', 'range_def', 'range_tab', 'ac']

@dataclass
class ffv1_encoder(): # ffv1 encoder
 slicecrc:bool = 'auto'
 coder:FFV1_ENCODER_CODER = 'rice'
 context:int = 0 
 ...


FFVHUFF_PRED = Literal['left', 'plane', 'median']

@dataclass
class ffvhuff(): # ffvhuff
 non_deterministic:bool = False
 pred:FFVHUFF_PRED = 'left'
 context:int = 0 
 ...


GENERIC_MPEGVIDEO_ENCODER_MPV_FLAGS = Literal['skip_rd', 'strict_gop', 'qp_rd', 'cbp_rd', 'naq', 'mv0']
GENERIC_MPEGVIDEO_ENCODER_SKIP_CMP = Literal['sad', 'sse', 'satd', 'dct', 'psnr', 'bit', 'rd', 'zero', 'vsad', 'vsse', 'nsse', 'dct264', 'dctmax', 'chroma', 'msad']
GENERIC_MPEGVIDEO_ENCODER_MOTION_EST = Literal['zero', 'epzs', 'xone']

@dataclass
class generic_mpegvideo_encoder(): # generic mpegvideo encoder
 mpv_flags:GENERIC_MPEGVIDEO_ENCODER_MPV_FLAGS = '0'
 luma_elim_threshold:int = 0
 chroma_elim_threshold:int = 0
 quantizer_noise_shaping:int = 0
 error_rate:int = 0
 qsquish:float = '0'
 rc_qmod_amp:float = '0'
 rc_qmod_freq:int = 0
 rc_eq:str = None
 rc_init_cplx:float = '0'
 rc_buf_aggressivity:float = '1'
 border_mask:float = '0'
 lmin:int = 236
 lmax:int = 3658
 skip_threshold:int = 0
 skip_factor:int = 0
 skip_exp:int = 0
 skip_cmp:GENERIC_MPEGVIDEO_ENCODER_SKIP_CMP = 'dctmax'
 sc_threshold:int = 0
 noise_reduction:int = 0
 ps:int = 0
 motion_est:GENERIC_MPEGVIDEO_ENCODER_MOTION_EST = 'epzs'
 mepc:int = 256
 mepre:int = 0
 intra_penalty:int = 0 
 ...


GIF_ENCODER_GIFFLAGS = Literal['offsetting', 'transdiff']

@dataclass
class GIF_encoder(): # GIF encoder
 gifflags:GIF_ENCODER_GIFFLAGS = 'offsetting+transdiff'
 gifimage:bool = False
 global_palette:bool = True 
 ...


H_263_ENCODER_MPV_FLAGS = Literal['skip_rd', 'strict_gop', 'qp_rd', 'cbp_rd', 'naq', 'mv0']
H_263_ENCODER_SKIP_CMP = Literal['sad', 'sse', 'satd', 'dct', 'psnr', 'bit', 'rd', 'zero', 'vsad', 'vsse', 'nsse', 'dct264', 'dctmax', 'chroma', 'msad']
H_263_ENCODER_MOTION_EST = Literal['zero', 'epzs', 'xone']

@dataclass
class H_263_encoder(): # H.263 encoder
 obmc:bool = False
 mb_info:int = 0
 mpv_flags:H_263_ENCODER_MPV_FLAGS = '0'
 luma_elim_threshold:int = 0
 chroma_elim_threshold:int = 0
 quantizer_noise_shaping:int = 0
 error_rate:int = 0
 qsquish:float = '0'
 rc_qmod_amp:float = '0'
 rc_qmod_freq:int = 0
 rc_eq:str = None
 rc_init_cplx:float = '0'
 rc_buf_aggressivity:float = '1'
 border_mask:float = '0'
 lmin:int = 236
 lmax:int = 3658
 skip_threshold:int = 0
 skip_factor:int = 0
 skip_exp:int = 0
 skip_cmp:H_263_ENCODER_SKIP_CMP = 'dctmax'
 sc_threshold:int = 0
 noise_reduction:int = 0
 ps:int = 0
 motion_est:H_263_ENCODER_MOTION_EST = 'epzs'
 mepc:int = 256
 mepre:int = 0
 intra_penalty:int = 0 
 ...


H_263P_ENCODER_MPV_FLAGS = Literal['skip_rd', 'strict_gop', 'qp_rd', 'cbp_rd', 'naq', 'mv0']
H_263P_ENCODER_SKIP_CMP = Literal['sad', 'sse', 'satd', 'dct', 'psnr', 'bit', 'rd', 'zero', 'vsad', 'vsse', 'nsse', 'dct264', 'dctmax', 'chroma', 'msad']
H_263P_ENCODER_MOTION_EST = Literal['zero', 'epzs', 'xone']

@dataclass
class H_263p_encoder(): # H.263p encoder
 umv:bool = False
 aiv:bool = False
 obmc:bool = False
 structured_slices:bool = False
 mpv_flags:H_263P_ENCODER_MPV_FLAGS = '0'
 luma_elim_threshold:int = 0
 chroma_elim_threshold:int = 0
 quantizer_noise_shaping:int = 0
 error_rate:int = 0
 qsquish:float = '0'
 rc_qmod_amp:float = '0'
 rc_qmod_freq:int = 0
 rc_eq:str = None
 rc_init_cplx:float = '0'
 rc_buf_aggressivity:float = '1'
 border_mask:float = '0'
 lmin:int = 236
 lmax:int = 3658
 skip_threshold:int = 0
 skip_factor:int = 0
 skip_exp:int = 0
 skip_cmp:H_263P_ENCODER_SKIP_CMP = 'dctmax'
 sc_threshold:int = 0
 noise_reduction:int = 0
 ps:int = 0
 motion_est:H_263P_ENCODER_MOTION_EST = 'epzs'
 mepc:int = 256
 mepre:int = 0
 intra_penalty:int = 0 
 ...


HAP_ENCODER_FORMAT = Literal['hap', 'hap_alpha', 'hap_q']
HAP_ENCODER_COMPRESSOR = Literal['none', 'snappy']

@dataclass
class Hap_encoder(): # Hap encoder
 format:HAP_ENCODER_FORMAT = 'hap'
 chunks:int = 1
 compressor:HAP_ENCODER_COMPRESSOR = 'snappy' 
 ...


HUFFYUV_PRED = Literal['left', 'plane', 'median']

@dataclass
class huffyuv(): # huffyuv
 non_deterministic:bool = False
 pred:HUFFYUV_PRED = 'left' 
 ...


JPEG_2000_ENCODER_FORMAT = Literal['j2k', 'jp2']
JPEG_2000_ENCODER_PRED = Literal['dwt97int', 'dwt53']
JPEG_2000_ENCODER_PROG = Literal['lrcp', 'rlcp', 'rpcl', 'pcrl', 'cprl']

@dataclass
class jpeg_2000_encoder(): # jpeg 2000 encoder
 format:JPEG_2000_ENCODER_FORMAT = 'jp2'
 tile_width:int = 256
 tile_height:int = 256
 pred:JPEG_2000_ENCODER_PRED = 'dwt97int'
 sop:int = 0
 eph:int = 0
 prog:JPEG_2000_ENCODER_PROG = 'lrcp'
 layer_rates:str = None 
 ...


JPEGLS_PRED = Literal['left', 'plane', 'median']

@dataclass
class jpegls(): # jpegls
 pred:JPEGLS_PRED = 'left' 
 ...


LJPEG_PRED = Literal['left', 'plane', 'median']

@dataclass
class ljpeg(): # ljpeg
 pred:LJPEG_PRED = 'left' 
 ...


MAGICYUV_PRED = Literal['left', 'gradient', 'median']

@dataclass
class magicyuv(): # magicyuv
 pred:MAGICYUV_PRED = 'left' 
 ...


MJPEG_ENCODER_MPV_FLAGS = Literal['skip_rd', 'strict_gop', 'qp_rd', 'cbp_rd', 'naq', 'mv0']
MJPEG_ENCODER_SKIP_CMP = Literal['sad', 'sse', 'satd', 'dct', 'psnr', 'bit', 'rd', 'zero', 'vsad', 'vsse', 'nsse', 'dct264', 'dctmax', 'chroma', 'msad']
MJPEG_ENCODER_HUFFMAN = Literal['default', 'optimal']

@dataclass
class mjpeg_encoder(): # mjpeg encoder
 mpv_flags:MJPEG_ENCODER_MPV_FLAGS = '0'
 luma_elim_threshold:int = 0
 chroma_elim_threshold:int = 0
 quantizer_noise_shaping:int = 0
 error_rate:int = 0
 qsquish:float = '0'
 rc_qmod_amp:float = '0'
 rc_qmod_freq:int = 0
 rc_eq:str = None
 rc_init_cplx:float = '0'
 rc_buf_aggressivity:float = '1'
 border_mask:float = '0'
 lmin:int = 236
 lmax:int = 3658
 skip_threshold:int = 0
 skip_factor:int = 0
 skip_exp:int = 0
 skip_cmp:MJPEG_ENCODER_SKIP_CMP = 'dctmax'
 sc_threshold:int = 0
 noise_reduction:int = 0
 ps:int = 0
 huffman:MJPEG_ENCODER_HUFFMAN = 'optimal'
 force_duplicated_matrix:bool = False 
 ...


MPEG1VIDEO_ENCODER_MPV_FLAGS = Literal['skip_rd', 'strict_gop', 'qp_rd', 'cbp_rd', 'naq', 'mv0']
MPEG1VIDEO_ENCODER_SKIP_CMP = Literal['sad', 'sse', 'satd', 'dct', 'psnr', 'bit', 'rd', 'zero', 'vsad', 'vsse', 'nsse', 'dct264', 'dctmax', 'chroma', 'msad']
MPEG1VIDEO_ENCODER_MOTION_EST = Literal['zero', 'epzs', 'xone']

@dataclass
class mpeg1video_encoder(): # mpeg1video encoder
 gop_timecode:str = None
 drop_frame_timecode:bool = False
 scan_offset:bool = False
 timecode_frame_start:int = -1
 b_strategy:int = 0
 b_sensitivity:int = 40
 brd_scale:int = 0
 mpv_flags:MPEG1VIDEO_ENCODER_MPV_FLAGS = '0'
 luma_elim_threshold:int = 0
 chroma_elim_threshold:int = 0
 quantizer_noise_shaping:int = 0
 error_rate:int = 0
 qsquish:float = '0'
 rc_qmod_amp:float = '0'
 rc_qmod_freq:int = 0
 rc_eq:str = None
 rc_init_cplx:float = '0'
 rc_buf_aggressivity:float = '1'
 border_mask:float = '0'
 lmin:int = 236
 lmax:int = 3658
 skip_threshold:int = 0
 skip_factor:int = 0
 skip_exp:int = 0
 skip_cmp:MPEG1VIDEO_ENCODER_SKIP_CMP = 'dctmax'
 sc_threshold:int = 0
 noise_reduction:int = 0
 ps:int = 0
 motion_est:MPEG1VIDEO_ENCODER_MOTION_EST = 'epzs'
 mepc:int = 256
 mepre:int = 0
 intra_penalty:int = 0 
 ...


MPEG2VIDEO_ENCODER_SEQ_DISP_EXT = Literal['auto', 'never', 'always']
MPEG2VIDEO_ENCODER_VIDEO_FORMAT = Literal['component', 'pal', 'ntsc', 'secam', 'mac', 'unspecified']
MPEG2VIDEO_ENCODER_MPV_FLAGS = Literal['skip_rd', 'strict_gop', 'qp_rd', 'cbp_rd', 'naq', 'mv0']
MPEG2VIDEO_ENCODER_SKIP_CMP = Literal['sad', 'sse', 'satd', 'dct', 'psnr', 'bit', 'rd', 'zero', 'vsad', 'vsse', 'nsse', 'dct264', 'dctmax', 'chroma', 'msad']
MPEG2VIDEO_ENCODER_MOTION_EST = Literal['zero', 'epzs', 'xone']

@dataclass
class mpeg2video_encoder(): # mpeg2video encoder
 gop_timecode:str = None
 drop_frame_timecode:bool = False
 scan_offset:bool = False
 timecode_frame_start:int = -1
 b_strategy:int = 0
 b_sensitivity:int = 40
 brd_scale:int = 0
 intra_vlc:bool = False
 non_linear_quant:bool = False
 alternate_scan:bool = False
 a53cc:bool = True
 seq_disp_ext:MPEG2VIDEO_ENCODER_SEQ_DISP_EXT = 'auto'
 video_format:MPEG2VIDEO_ENCODER_VIDEO_FORMAT = 'unspecified'
 mpv_flags:MPEG2VIDEO_ENCODER_MPV_FLAGS = '0'
 luma_elim_threshold:int = 0
 chroma_elim_threshold:int = 0
 quantizer_noise_shaping:int = 0
 error_rate:int = 0
 qsquish:float = '0'
 rc_qmod_amp:float = '0'
 rc_qmod_freq:int = 0
 rc_eq:str = None
 rc_init_cplx:float = '0'
 rc_buf_aggressivity:float = '1'
 border_mask:float = '0'
 lmin:int = 236
 lmax:int = 3658
 skip_threshold:int = 0
 skip_factor:int = 0
 skip_exp:int = 0
 skip_cmp:MPEG2VIDEO_ENCODER_SKIP_CMP = 'dctmax'
 sc_threshold:int = 0
 noise_reduction:int = 0
 ps:int = 0
 motion_est:MPEG2VIDEO_ENCODER_MOTION_EST = 'epzs'
 mepc:int = 256
 mepre:int = 0
 intra_penalty:int = 0 
 ...


MPEG4_ENCODER_MPV_FLAGS = Literal['skip_rd', 'strict_gop', 'qp_rd', 'cbp_rd', 'naq', 'mv0']
MPEG4_ENCODER_SKIP_CMP = Literal['sad', 'sse', 'satd', 'dct', 'psnr', 'bit', 'rd', 'zero', 'vsad', 'vsse', 'nsse', 'dct264', 'dctmax', 'chroma', 'msad']
MPEG4_ENCODER_MOTION_EST = Literal['zero', 'epzs', 'xone']

@dataclass
class MPEG4_encoder(): # MPEG4 encoder
 data_partitioning:bool = False
 alternate_scan:bool = False
 mpeg_quant:int = 0
 b_strategy:int = 0
 b_sensitivity:int = 40
 brd_scale:int = 0
 mpv_flags:MPEG4_ENCODER_MPV_FLAGS = '0'
 luma_elim_threshold:int = 0
 chroma_elim_threshold:int = 0
 quantizer_noise_shaping:int = 0
 error_rate:int = 0
 qsquish:float = '0'
 rc_qmod_amp:float = '0'
 rc_qmod_freq:int = 0
 rc_eq:str = None
 rc_init_cplx:float = '0'
 rc_buf_aggressivity:float = '1'
 border_mask:float = '0'
 lmin:int = 236
 lmax:int = 3658
 skip_threshold:int = 0
 skip_factor:int = 0
 skip_exp:int = 0
 skip_cmp:MPEG4_ENCODER_SKIP_CMP = 'dctmax'
 sc_threshold:int = 0
 noise_reduction:int = 0
 ps:int = 0
 motion_est:MPEG4_ENCODER_MOTION_EST = 'epzs'
 mepc:int = 256
 mepre:int = 0
 intra_penalty:int = 0 
 ...




@dataclass
class ProRes_encoder(): # ProRes encoder
 vendor:str = "fmpg" 
 ...




@dataclass
class RoQ(): # RoQ
 quake3_compat:bool = True 
 ...




@dataclass
class rpza(): # rpza
 skip_frame_thresh:int = 1
 start_one_color_thresh:int = 1
 continue_one_color_thresh:int = 0
 sixteen_color_thresh:int = 1 
 ...




@dataclass
class sgi(): # sgi
 rle:int = 1 
 ...


SNOW_ENCODER_MOTION_EST = Literal['zero', 'epzs', 'xone', 'iter']
SNOW_ENCODER_PRED = Literal['dwt97', 'dwt53']

@dataclass
class snow_encoder(): # snow encoder
 motion_est:SNOW_ENCODER_MOTION_EST = 'epzs'
 memc_only:bool = False
 no_bitstream:bool = False
 intra_penalty:int = 0
 iterative_dia_size:int = 0
 sc_threshold:int = 0
 pred:SNOW_ENCODER_PRED = 'dwt97'
 rc_eq:str = None 
 ...




@dataclass
class sunrast(): # sunrast
 rle:int = 1 
 ...


SVQ1ENC_MOTION_EST = Literal['zero', 'epzs', 'xone']

@dataclass
class svq1enc(): # svq1enc
 motion_est:SVQ1ENC_MOTION_EST = dataclasses_field(default='epzs', metadata='motion-est') 
 ...




@dataclass
class targa(): # targa
 rle:int = 1 
 ...


TIFF_ENCODER_COMPRESSION_ALGO = Literal['packbits', 'raw', 'lzw', 'deflate']

@dataclass
class TIFF_encoder(): # TIFF encoder
 dpi:int = 72
 compression_algo:TIFF_ENCODER_COMPRESSION_ALGO = 'packbits' 
 ...


UTVIDEO_PRED = Literal['none', 'left', 'gradient', 'median']

@dataclass
class utvideo(): # utvideo
 pred:UTVIDEO_PRED = 'left' 
 ...


VBN_ENCODER_FORMAT = Literal['raw', 'dxt1', 'dxt5']

@dataclass
class VBN_encoder(): # VBN encoder
 format:VBN_ENCODER_FORMAT = 'dxt5' 
 ...


SMPTE_VC_2_ENCODER_WAVELET_TYPE = Literal['9_7', '5_3', 'haar', 'haar_noshift']
SMPTE_VC_2_ENCODER_QM = Literal['default', 'color', 'flat']

@dataclass
class SMPTE_VC_2_encoder(): # SMPTE VC-2 encoder
 tolerance:float = '5'
 slice_width:int = 32
 slice_height:int = 16
 wavelet_depth:int = 4
 wavelet_type:SMPTE_VC_2_ENCODER_WAVELET_TYPE = '9_7'
 qm:SMPTE_VC_2_ENCODER_QM = 'default' 
 ...


AAC_ENCODER_AAC_CODER = Literal['anmr', 'twoloop', 'fast']

@dataclass
class AAC_encoder(): # AAC encoder
 aac_coder:AAC_ENCODER_AAC_CODER = 'twoloop'
 aac_ms:bool = 'auto'
 aac_is:bool = True
 aac_pns:bool = True
 aac_tns:bool = True
 aac_ltp:bool = False
 aac_pred:bool = False
 aac_pce:bool = False 
 ...


AC_3_ENCODER_ROOM_TYPE = Literal['notindicated', 'large', 'small']
AC_3_ENCODER_DSUR_MODE = Literal['notindicated', 'on', 'off']
AC_3_ENCODER_DMIX_MODE = Literal['notindicated', 'ltrt', 'loro', 'dplii']
AC_3_ENCODER_DSUREX_MODE = Literal['notindicated', 'on', 'off', 'dpliiz']
AC_3_ENCODER_AD_CONV_TYPE = Literal['standard', 'hdcd']
AC_3_ENCODER_CHANNEL_COUPLING = Literal['auto']

@dataclass
class AC_3_Encoder(): # AC-3 Encoder
 center_mixlev:float = '0.594604'
 surround_mixlev:float = '0.5'
 mixing_level:int = -1
 room_type:AC_3_ENCODER_ROOM_TYPE = '-1'
 per_frame_metadata:bool = False
 copyright:int = -1
 dialnorm:int = -31
 dsur_mode:AC_3_ENCODER_DSUR_MODE = '-1'
 original:int = -1
 dmix_mode:AC_3_ENCODER_DMIX_MODE = '-1'
 ltrt_cmixlev:float = '-1'
 ltrt_surmixlev:float = '-1'
 loro_cmixlev:float = '-1'
 loro_surmixlev:float = '-1'
 dsurex_mode:AC_3_ENCODER_DSUREX_MODE = '-1'
 dheadphone_mode:AC_3_ENCODER_DSUR_MODE = '-1'
 ad_conv_type:AC_3_ENCODER_AD_CONV_TYPE = '-1'
 stereo_rematrixing:bool = True
 channel_coupling:AC_3_ENCODER_CHANNEL_COUPLING = 'auto'
 cpl_start_band:AC_3_ENCODER_CHANNEL_COUPLING = 'auto' 
 ...




@dataclass
class alacenc(): # alacenc
 min_prediction_order:int = 4
 max_prediction_order:int = 6 
 ...




@dataclass
class DCA__DTS_Coherent_Acoustics_(): # DCA (DTS Coherent Acoustics)
 dca_adpcm:bool = False 
 ...


E_AC_3_ENCODER_ROOM_TYPE = Literal['notindicated', 'large', 'small']
E_AC_3_ENCODER_DSUR_MODE = Literal['notindicated', 'on', 'off']
E_AC_3_ENCODER_DMIX_MODE = Literal['notindicated', 'ltrt', 'loro', 'dplii']
E_AC_3_ENCODER_DSUREX_MODE = Literal['notindicated', 'on', 'off', 'dpliiz']
E_AC_3_ENCODER_AD_CONV_TYPE = Literal['standard', 'hdcd']
E_AC_3_ENCODER_CHANNEL_COUPLING = Literal['auto']

@dataclass
class E_AC_3_Encoder(): # E-AC-3 Encoder
 mixing_level:int = -1
 room_type:E_AC_3_ENCODER_ROOM_TYPE = '-1'
 per_frame_metadata:bool = False
 copyright:int = -1
 dialnorm:int = -31
 dsur_mode:E_AC_3_ENCODER_DSUR_MODE = '-1'
 original:int = -1
 dmix_mode:E_AC_3_ENCODER_DMIX_MODE = '-1'
 ltrt_cmixlev:float = '-1'
 ltrt_surmixlev:float = '-1'
 loro_cmixlev:float = '-1'
 loro_surmixlev:float = '-1'
 dsurex_mode:E_AC_3_ENCODER_DSUREX_MODE = '-1'
 dheadphone_mode:E_AC_3_ENCODER_DSUR_MODE = '-1'
 ad_conv_type:E_AC_3_ENCODER_AD_CONV_TYPE = '-1'
 stereo_rematrixing:bool = True
 channel_coupling:E_AC_3_ENCODER_CHANNEL_COUPLING = 'auto'
 cpl_start_band:E_AC_3_ENCODER_CHANNEL_COUPLING = 'auto' 
 ...


FLAC_ENCODER_LPC_TYPE = Literal['none', 'fixed', 'levinson', 'cholesky']
FLAC_ENCODER_PREDICTION_ORDER_METHOD = Literal['estimation', '2level', '4level', '8level', 'search', 'log']
FLAC_ENCODER_CH_MODE = Literal['auto', 'indep', 'left_side', 'right_side', 'mid_side']

@dataclass
class FLAC_encoder(): # FLAC encoder
 lpc_coeff_precision:int = 15
 lpc_type:FLAC_ENCODER_LPC_TYPE = '-1'
 lpc_passes:int = 2
 min_partition_order:int = -1
 max_partition_order:int = -1
 prediction_order_method:FLAC_ENCODER_PREDICTION_ORDER_METHOD = '-1'
 ch_mode:FLAC_ENCODER_CH_MODE = 'auto'
 exact_rice_parameters:bool = False
 multi_dim_quant:bool = False
 min_prediction_order:int = -1
 max_prediction_order:int = -1 
 ...




@dataclass
class Opus_encoder(): # Opus encoder
 opus_delay:float = '360'
 apply_phase_inv:bool = True 
 ...




@dataclass
class sbc_encoder(): # sbc encoder
 sbc_delay:str = '0.013'
 msbc:bool = False 
 ...




@dataclass
class WavPack_encoder(): # WavPack encoder
 joint_stereo:bool = 'auto'
 optimize_mono:bool = False 
 ...




@dataclass
class ADPCM_encoder(): # ADPCM encoder
 block_size:int = 1024 
 ...




@dataclass
class g726(): # g726
 code_size:int = 4 
 ...




@dataclass
class VOBSUB_subtitle_encoder(): # VOBSUB subtitle encoder
 palette:str = None
 even_rows_fix:bool = False 
 ...




@dataclass
class MOV_text_enoder(): # MOV text enoder
 height:int = 0 
 ...


AT_AAC_ENC_AAC_AT_MODE = Literal['auto', 'cbr', 'abr', 'cvbr', 'vbr']

@dataclass
class at_aac_enc(): # at_aac_enc
 aac_at_mode:AT_AAC_ENC_AAC_AT_MODE = 'auto'
 aac_at_quality:int = 0 
 ...


AT_ALAC_ENC_AAC_AT_MODE = Literal['auto', 'cbr', 'abr', 'cvbr', 'vbr']

@dataclass
class at_alac_enc(): # at_alac_enc
 aac_at_mode:AT_ALAC_ENC_AAC_AT_MODE = 'auto'
 aac_at_quality:int = 0 
 ...


AT_ILBC_ENC_AAC_AT_MODE = Literal['auto', 'cbr', 'abr', 'cvbr', 'vbr']

@dataclass
class at_ilbc_enc(): # at_ilbc_enc
 aac_at_mode:AT_ILBC_ENC_AAC_AT_MODE = 'auto'
 aac_at_quality:int = 0 
 ...


AT_PCM_ALAW_ENC_AAC_AT_MODE = Literal['auto', 'cbr', 'abr', 'cvbr', 'vbr']

@dataclass
class at_pcm_alaw_enc(): # at_pcm_alaw_enc
 aac_at_mode:AT_PCM_ALAW_ENC_AAC_AT_MODE = 'auto'
 aac_at_quality:int = 0 
 ...


AT_PCM_MULAW_ENC_AAC_AT_MODE = Literal['auto', 'cbr', 'abr', 'cvbr', 'vbr']

@dataclass
class at_pcm_mulaw_enc(): # at_pcm_mulaw_enc
 aac_at_mode:AT_PCM_MULAW_ENC_AAC_AT_MODE = 'auto'
 aac_at_quality:int = 0 
 ...


LIBAOM_AV1_ENCODER_AQ_MODE = Literal['none', 'variance', 'complexity', 'cyclic']
LIBAOM_AV1_ENCODER_ERROR_RESILIENCE = Literal['default']
LIBAOM_AV1_ENCODER_USAGE = Literal['good', 'realtime', 'allintra']
LIBAOM_AV1_ENCODER_TUNE = Literal['psnr', 'ssim']

@dataclass
class libaom_av1_encoder(): # libaom-av1 encoder
 cpu_used:int = dataclasses_field(default=1, metadata='cpu-used')
 auto_alt_ref:int = dataclasses_field(default=-1, metadata='auto-alt-ref')
 lag_in_frames:int = dataclasses_field(default=-1, metadata='lag-in-frames')
 arnr_max_frames:int = dataclasses_field(default=-1, metadata='arnr-max-frames')
 arnr_strength:int = dataclasses_field(default=-1, metadata='arnr-strength')
 aq_mode:LIBAOM_AV1_ENCODER_AQ_MODE = dataclasses_field(default='-1', metadata='aq-mode')
 error_resilience:LIBAOM_AV1_ENCODER_ERROR_RESILIENCE = dataclasses_field(default='0', metadata='error-resilience')
 crf:int = -1
 static_thresh:int = dataclasses_field(default=0, metadata='static-thresh')
 drop_threshold:int = dataclasses_field(default=0, metadata='drop-threshold')
 denoise_noise_level:int = dataclasses_field(default=-1, metadata='denoise-noise-level')
 denoise_block_size:int = dataclasses_field(default=-1, metadata='denoise-block-size')
 undershoot_pct:int = dataclasses_field(default=-1, metadata='undershoot-pct')
 overshoot_pct:int = dataclasses_field(default=-1, metadata='overshoot-pct')
 minsection_pct:int = dataclasses_field(default=-1, metadata='minsection-pct')
 maxsection_pct:int = dataclasses_field(default=-1, metadata='maxsection-pct')
 frame_parallel:bool = dataclasses_field(default='auto', metadata='frame-parallel')
 tiles:IMAGE_SIZES = None
 tile_columns:int = dataclasses_field(default=-1, metadata='tile-columns')
 tile_rows:int = dataclasses_field(default=-1, metadata='tile-rows')
 row_mt:bool = dataclasses_field(default='auto', metadata='row-mt')
 enable_cdef:bool = dataclasses_field(default='auto', metadata='enable-cdef')
 enable_global_motion:bool = dataclasses_field(default='auto', metadata='enable-global-motion')
 enable_intrabc:bool = dataclasses_field(default='auto', metadata='enable-intrabc')
 enable_restoration:bool = dataclasses_field(default='auto', metadata='enable-restoration')
 usage:LIBAOM_AV1_ENCODER_USAGE = 'good'
 tune:LIBAOM_AV1_ENCODER_TUNE = '-1'
 still_picture:bool = dataclasses_field(default=False, metadata='still-picture')
 enable_rect_partitions:bool = dataclasses_field(default='auto', metadata='enable-rect-partitions')
 enable_1to4_partitions:bool = dataclasses_field(default='auto', metadata='enable-1to4-partitions')
 enable_ab_partitions:bool = dataclasses_field(default='auto', metadata='enable-ab-partitions')
 enable_angle_delta:bool = dataclasses_field(default='auto', metadata='enable-angle-delta')
 enable_cfl_intra:bool = dataclasses_field(default='auto', metadata='enable-cfl-intra')
 enable_filter_intra:bool = dataclasses_field(default='auto', metadata='enable-filter-intra')
 enable_intra_edge_filter:bool = dataclasses_field(default='auto', metadata='enable-intra-edge-filter')
 enable_smooth_intra:bool = dataclasses_field(default='auto', metadata='enable-smooth-intra')
 enable_paeth_intra:bool = dataclasses_field(default='auto', metadata='enable-paeth-intra')
 enable_palette:bool = dataclasses_field(default='auto', metadata='enable-palette')
 enable_flip_idtx:bool = dataclasses_field(default='auto', metadata='enable-flip-idtx')
 enable_tx64:bool = dataclasses_field(default='auto', metadata='enable-tx64')
 reduced_tx_type_set:bool = dataclasses_field(default='auto', metadata='reduced-tx-type-set')
 use_intra_dct_only:bool = dataclasses_field(default='auto', metadata='use-intra-dct-only')
 use_inter_dct_only:bool = dataclasses_field(default='auto', metadata='use-inter-dct-only')
 use_intra_default_tx_only:bool = dataclasses_field(default='auto', metadata='use-intra-default-tx-only')
 enable_ref_frame_mvs:bool = dataclasses_field(default='auto', metadata='enable-ref-frame-mvs')
 enable_reduced_reference_set:bool = dataclasses_field(default='auto', metadata='enable-reduced-reference-set')
 enable_obmc:bool = dataclasses_field(default='auto', metadata='enable-obmc')
 enable_dual_filter:bool = dataclasses_field(default='auto', metadata='enable-dual-filter')
 enable_diff_wtd_comp:bool = dataclasses_field(default='auto', metadata='enable-diff-wtd-comp')
 enable_dist_wtd_comp:bool = dataclasses_field(default='auto', metadata='enable-dist-wtd-comp')
 enable_onesided_comp:bool = dataclasses_field(default='auto', metadata='enable-onesided-comp')
 enable_interinter_wedge:bool = dataclasses_field(default='auto', metadata='enable-interinter-wedge')
 enable_interintra_wedge:bool = dataclasses_field(default='auto', metadata='enable-interintra-wedge')
 enable_masked_comp:bool = dataclasses_field(default='auto', metadata='enable-masked-comp')
 enable_interintra_comp:bool = dataclasses_field(default='auto', metadata='enable-interintra-comp')
 enable_smooth_interintra:bool = dataclasses_field(default='auto', metadata='enable-smooth-interintra')
 aom_params:dict = dataclasses_field(default=None, metadata='aom-params') 
 ...




@dataclass
class libjxl(): # libjxl
 effort:int = 7
 distance:float = '-1'
 modular:int = 0 
 ...




@dataclass
class libmp3lame_encoder(): # libmp3lame encoder
 reservoir:bool = True
 joint_stereo:bool = True
 abr:bool = False 
 ...




@dataclass
class libopencore_amrnb(): # libopencore_amrnb
 dtx:int = 0 
 ...


LIBOPENJPEG_FORMAT = Literal['j2k', 'jp2']
LIBOPENJPEG_PROFILE = Literal['jpeg2000', 'cinema2k', 'cinema4k']
LIBOPENJPEG_CINEMA_MODE = Literal['off', '2k_24', '2k_48', '4k_24']
LIBOPENJPEG_PROG_ORDER = Literal['lrcp', 'rlcp', 'rpcl', 'pcrl', 'cprl']

@dataclass
class libopenjpeg(): # libopenjpeg
 format:LIBOPENJPEG_FORMAT = 'jp2'
 profile:LIBOPENJPEG_PROFILE = 'jpeg2000'
 cinema_mode:LIBOPENJPEG_CINEMA_MODE = 'off'
 prog_order:LIBOPENJPEG_PROG_ORDER = 'lrcp'
 numresolution:int = 6
 irreversible:int = 0
 disto_alloc:int = 1
 fixed_quality:int = 0 
 ...


LIBOPUS_APPLICATION = Literal['voip', 'audio', 'lowdelay']
LIBOPUS_VBR = Literal['off', 'on', 'constrained']

@dataclass
class libopus(): # libopus
 application:LIBOPUS_APPLICATION = 'audio'
 frame_duration:float = '20'
 packet_loss:int = 0
 fec:bool = False
 vbr:LIBOPUS_VBR = 'on'
 mapping_family:int = -1
 apply_phase_inv:bool = True 
 ...




@dataclass
class librav1e(): # librav1e
 qp:int = -1
 speed:int = -1
 tiles:int = 0
 tile_rows:int = dataclasses_field(default=0, metadata='tile-rows')
 tile_columns:int = dataclasses_field(default=0, metadata='tile-columns')
 rav1e_params:dict = dataclasses_field(default=None, metadata='rav1e-params') 
 ...




@dataclass
class libspeex(): # libspeex
 abr:int = 0
 cbr_quality:int = 8
 frames_per_packet:int = 1
 vad:int = 0
 dtx:int = 0 
 ...


LIBSVTAV1_HIELEVEL = Literal['3level', '4level']
LIBSVTAV1_TIER = Literal['main', 'high']

@dataclass
class libsvtav1(): # libsvtav1
 hielevel:LIBSVTAV1_HIELEVEL = '-1'
 la_depth:int = -1
 tier:LIBSVTAV1_TIER = '-1'
 preset:int = -1
 crf:int = 0
 qp:int = 0
 sc_detection:bool = 'auto'
 tile_columns:int = -1
 tile_rows:int = -1
 svtav1_params:dict = dataclasses_field(default=None, metadata='svtav1-params') 
 ...




@dataclass
class libvorbis(): # libvorbis
 iblock:float = '0' 
 ...


LIBVPX_VP8_ENCODER_ARNR_TYPE = Literal['backward', 'forward', 'centered']
LIBVPX_VP8_ENCODER_TUNE = Literal['psnr', 'ssim']
LIBVPX_VP8_ENCODER_DEADLINE = Literal['best', 'good', 'realtime']
LIBVPX_VP8_ENCODER_ERROR_RESILIENT = Literal['default', 'partitions']
LIBVPX_VP8_ENCODER_VP8FLAGS = Literal['error_resilient', 'altref']

@dataclass
class libvpx_vp8_encoder(): # libvpx-vp8 encoder
 lag_in_frames:int = dataclasses_field(default=-1, metadata='lag-in-frames')
 arnr_maxframes:int = dataclasses_field(default=-1, metadata='arnr-maxframes')
 arnr_strength:int = dataclasses_field(default=-1, metadata='arnr-strength')
 arnr_type:LIBVPX_VP8_ENCODER_ARNR_TYPE = dataclasses_field(default='-1', metadata='arnr-type')
 tune:LIBVPX_VP8_ENCODER_TUNE = '-1'
 deadline:LIBVPX_VP8_ENCODER_DEADLINE = 'good'
 error_resilient:LIBVPX_VP8_ENCODER_ERROR_RESILIENT = dataclasses_field(default='0', metadata='error-resilient')
 max_intra_rate:int = dataclasses_field(default=-1, metadata='max-intra-rate')
 crf:int = -1
 static_thresh:int = dataclasses_field(default=0, metadata='static-thresh')
 drop_threshold:int = dataclasses_field(default=0, metadata='drop-threshold')
 noise_sensitivity:int = dataclasses_field(default=0, metadata='noise-sensitivity')
 undershoot_pct:int = dataclasses_field(default=-1, metadata='undershoot-pct')
 overshoot_pct:int = dataclasses_field(default=-1, metadata='overshoot-pct')
 ts_parameters:dict = dataclasses_field(default=None, metadata='ts-parameters')
 auto_alt_ref:int = dataclasses_field(default=-1, metadata='auto-alt-ref')
 cpu_used:int = dataclasses_field(default=1, metadata='cpu-used')
 speed:int = 1
 quality:LIBVPX_VP8_ENCODER_DEADLINE = 'good'
 vp8flags:LIBVPX_VP8_ENCODER_VP8FLAGS = '0'
 arnr_max_frames:int = 0
 arnr_strength:int = 3
 arnr_type:int = 3
 rc_lookahead:int = 25
 sharpness:int = -1 
 ...


LIBVPX_VP9_ENCODER_ARNR_TYPE = Literal['backward', 'forward', 'centered']
LIBVPX_VP9_ENCODER_TUNE = Literal['psnr', 'ssim']
LIBVPX_VP9_ENCODER_DEADLINE = Literal['best', 'good', 'realtime']
LIBVPX_VP9_ENCODER_ERROR_RESILIENT = Literal['default', 'partitions']
LIBVPX_VP9_ENCODER_AQ_MODE = Literal['none', 'variance', 'complexity', 'cyclic', 'equator360']
LIBVPX_VP9_ENCODER_TUNE_CONTENT = Literal['default', 'screen', 'film']
LIBVPX_VP9_ENCODER_VP8FLAGS = Literal['error_resilient', 'altref']

@dataclass
class libvpx_vp9_encoder(): # libvpx-vp9 encoder
 lag_in_frames:int = dataclasses_field(default=-1, metadata='lag-in-frames')
 arnr_maxframes:int = dataclasses_field(default=-1, metadata='arnr-maxframes')
 arnr_strength:int = dataclasses_field(default=-1, metadata='arnr-strength')
 arnr_type:LIBVPX_VP9_ENCODER_ARNR_TYPE = dataclasses_field(default='-1', metadata='arnr-type')
 tune:LIBVPX_VP9_ENCODER_TUNE = '-1'
 deadline:LIBVPX_VP9_ENCODER_DEADLINE = 'good'
 error_resilient:LIBVPX_VP9_ENCODER_ERROR_RESILIENT = dataclasses_field(default='0', metadata='error-resilient')
 max_intra_rate:int = dataclasses_field(default=-1, metadata='max-intra-rate')
 crf:int = -1
 static_thresh:int = dataclasses_field(default=0, metadata='static-thresh')
 drop_threshold:int = dataclasses_field(default=0, metadata='drop-threshold')
 noise_sensitivity:int = dataclasses_field(default=0, metadata='noise-sensitivity')
 undershoot_pct:int = dataclasses_field(default=-1, metadata='undershoot-pct')
 overshoot_pct:int = dataclasses_field(default=-1, metadata='overshoot-pct')
 ts_parameters:dict = dataclasses_field(default=None, metadata='ts-parameters')
 auto_alt_ref:int = dataclasses_field(default=-1, metadata='auto-alt-ref')
 cpu_used:int = dataclasses_field(default=1, metadata='cpu-used')
 lossless:int = -1
 tile_columns:int = dataclasses_field(default=-1, metadata='tile-columns')
 tile_rows:int = dataclasses_field(default=-1, metadata='tile-rows')
 frame_parallel:bool = dataclasses_field(default='auto', metadata='frame-parallel')
 aq_mode:LIBVPX_VP9_ENCODER_AQ_MODE = dataclasses_field(default='-1', metadata='aq-mode')
 level:float = '-1'
 row_mt:bool = dataclasses_field(default='auto', metadata='row-mt')
 tune_content:LIBVPX_VP9_ENCODER_TUNE_CONTENT = dataclasses_field(default='-1', metadata='tune-content')
 corpus_complexity:int = dataclasses_field(default=-1, metadata='corpus-complexity')
 enable_tpl:bool = dataclasses_field(default='auto', metadata='enable-tpl')
 min_gf_interval:int = dataclasses_field(default=-1, metadata='min-gf-interval')
 speed:int = 1
 quality:LIBVPX_VP9_ENCODER_DEADLINE = 'good'
 vp8flags:LIBVPX_VP9_ENCODER_VP8FLAGS = '0'
 arnr_max_frames:int = 0
 arnr_strength:int = 3
 arnr_type:int = 3
 rc_lookahead:int = 25
 sharpness:int = -1 
 ...


LIBWEBP_ENCODER_PRESET = Literal['none', 'default', 'picture', 'photo', 'drawing', 'icon', 'text']

@dataclass
class libwebp_encoder(): # libwebp encoder
 lossless:int = 0
 preset:LIBWEBP_ENCODER_PRESET = 'none'
 cr_threshold:int = 0
 cr_size:int = 16
 quality:float = '75' 
 ...


LIBX264_AQ_MODE = Literal['none', 'variance', 'autovariance', 'autovariance-biased']
LIBX264_WEIGHTP = Literal['none', 'simple', 'smart']
LIBX264_B_PYRAMID = Literal['none', 'strict', 'normal']
LIBX264_DIRECT_PRED = Literal['none', 'spatial', 'temporal', 'auto']
LIBX264_NAL_HRD = Literal['none', 'vbr', 'cbr']
LIBX264_ME_METHOD = Literal['dia', 'hex', 'umh', 'esa', 'tesa']
LIBX264_CODER = Literal['default', 'cavlc', 'cabac', 'vlc', 'ac']

@dataclass
class libx264(): # libx264
 preset:str = "medium"
 tune:str = None
 profile:str = None
 fastfirstpass:bool = True
 level:str = None
 passlogfile:str = None
 wpredp:str = None
 a53cc:bool = True
 x264opts:str = None
 crf:float = '-1'
 crf_max:float = '-1'
 qp:int = -1
 aq_mode:LIBX264_AQ_MODE = dataclasses_field(default='-1', metadata='aq-mode')
 aq_strength:float = dataclasses_field(default='-1', metadata='aq-strength')
 psy:bool = 'auto'
 psy_rd:str = dataclasses_field(default=None, metadata='psy-rd')
 rc_lookahead:int = dataclasses_field(default=-1, metadata='rc-lookahead')
 weightb:bool = 'auto'
 weightp:LIBX264_WEIGHTP = '-1'
 ssim:bool = 'auto'
 intra_refresh:bool = dataclasses_field(default='auto', metadata='intra-refresh')
 bluray_compat:bool = dataclasses_field(default='auto', metadata='bluray-compat')
 b_bias:int = dataclasses_field(default='INT_MIN', metadata='b-bias')
 b_pyramid:LIBX264_B_PYRAMID = dataclasses_field(default='-1', metadata='b-pyramid')
 mixed_refs:bool = dataclasses_field(default='auto', metadata='mixed-refs')
 _8x8dct:bool = dataclasses_field(default='auto', metadata='8x8dct')
 fast_pskip:bool = dataclasses_field(default='auto', metadata='fast-pskip')
 aud:bool = 'auto'
 mbtree:bool = 'auto'
 deblock:str = None
 cplxblur:float = '-1'
 partitions:str = None
 direct_pred:LIBX264_DIRECT_PRED = dataclasses_field(default='-1', metadata='direct-pred')
 slice_max_size:int = dataclasses_field(default=-1, metadata='slice-max-size')
 stats:str = None
 nal_hrd:LIBX264_NAL_HRD = dataclasses_field(default='-1', metadata='nal-hrd')
 avcintra_class:int = dataclasses_field(default=-1, metadata='avcintra-class')
 me_method:LIBX264_ME_METHOD = '-1'
 motion_est:LIBX264_ME_METHOD = dataclasses_field(default='-1', metadata='motion-est')
 forced_idr:bool = dataclasses_field(default=False, metadata='forced-idr')
 coder:LIBX264_CODER = 'default'
 b_strategy:int = -1
 chromaoffset:int = 0
 sc_threshold:int = -1
 noise_reduction:int = -1
 udu_sei:bool = False
 x264_params:dict = dataclasses_field(default=None, metadata='x264-params') 
 ...


LIBX264RGB_AQ_MODE = Literal['none', 'variance', 'autovariance', 'autovariance-biased']
LIBX264RGB_WEIGHTP = Literal['none', 'simple', 'smart']
LIBX264RGB_B_PYRAMID = Literal['none', 'strict', 'normal']
LIBX264RGB_DIRECT_PRED = Literal['none', 'spatial', 'temporal', 'auto']
LIBX264RGB_NAL_HRD = Literal['none', 'vbr', 'cbr']
LIBX264RGB_ME_METHOD = Literal['dia', 'hex', 'umh', 'esa', 'tesa']
LIBX264RGB_CODER = Literal['default', 'cavlc', 'cabac', 'vlc', 'ac']

@dataclass
class libx264rgb(): # libx264rgb
 preset:str = "medium"
 tune:str = None
 profile:str = None
 fastfirstpass:bool = True
 level:str = None
 passlogfile:str = None
 wpredp:str = None
 a53cc:bool = True
 x264opts:str = None
 crf:float = '-1'
 crf_max:float = '-1'
 qp:int = -1
 aq_mode:LIBX264RGB_AQ_MODE = dataclasses_field(default='-1', metadata='aq-mode')
 aq_strength:float = dataclasses_field(default='-1', metadata='aq-strength')
 psy:bool = 'auto'
 psy_rd:str = dataclasses_field(default=None, metadata='psy-rd')
 rc_lookahead:int = dataclasses_field(default=-1, metadata='rc-lookahead')
 weightb:bool = 'auto'
 weightp:LIBX264RGB_WEIGHTP = '-1'
 ssim:bool = 'auto'
 intra_refresh:bool = dataclasses_field(default='auto', metadata='intra-refresh')
 bluray_compat:bool = dataclasses_field(default='auto', metadata='bluray-compat')
 b_bias:int = dataclasses_field(default='INT_MIN', metadata='b-bias')
 b_pyramid:LIBX264RGB_B_PYRAMID = dataclasses_field(default='-1', metadata='b-pyramid')
 mixed_refs:bool = dataclasses_field(default='auto', metadata='mixed-refs')
 _8x8dct:bool = dataclasses_field(default='auto', metadata='8x8dct')
 fast_pskip:bool = dataclasses_field(default='auto', metadata='fast-pskip')
 aud:bool = 'auto'
 mbtree:bool = 'auto'
 deblock:str = None
 cplxblur:float = '-1'
 partitions:str = None
 direct_pred:LIBX264RGB_DIRECT_PRED = dataclasses_field(default='-1', metadata='direct-pred')
 slice_max_size:int = dataclasses_field(default=-1, metadata='slice-max-size')
 stats:str = None
 nal_hrd:LIBX264RGB_NAL_HRD = dataclasses_field(default='-1', metadata='nal-hrd')
 avcintra_class:int = dataclasses_field(default=-1, metadata='avcintra-class')
 me_method:LIBX264RGB_ME_METHOD = '-1'
 motion_est:LIBX264RGB_ME_METHOD = dataclasses_field(default='-1', metadata='motion-est')
 forced_idr:bool = dataclasses_field(default=False, metadata='forced-idr')
 coder:LIBX264RGB_CODER = 'default'
 b_strategy:int = -1
 chromaoffset:int = 0
 sc_threshold:int = -1
 noise_reduction:int = -1
 udu_sei:bool = False
 x264_params:dict = dataclasses_field(default=None, metadata='x264-params') 
 ...




@dataclass
class libx265(): # libx265
 crf:float = '-1'
 qp:int = -1
 forced_idr:bool = dataclasses_field(default=False, metadata='forced-idr')
 preset:str = None
 tune:str = None
 profile:str = None
 udu_sei:bool = False
 a53cc:bool = True
 x265_params:dict = dataclasses_field(default=None, metadata='x265-params') 
 ...


LIBXVID_SSIM = Literal['off', 'avg', 'frame']

@dataclass
class libxvid(): # libxvid
 lumi_aq:int = 0
 variance_aq:int = 0
 ssim:LIBXVID_SSIM = 'off'
 ssim_acc:int = 2
 gmc:int = 0
 me_quality:int = 4
 mpeg_quant:int = 0 
 ...


H264_VIDEOTOOLBOX_PROFILE = Literal['baseline', 'main', 'high', 'extended']
H264_VIDEOTOOLBOX_LEVEL = Literal['1.3', '3.0', '3.1', '3.2', '4.0', '4.1', '4.2', '5.0', '5.1', '5.2']
H264_VIDEOTOOLBOX_CODER = Literal['cavlc', 'vlc', 'cabac', 'ac']

@dataclass
class h264_videotoolbox(): # h264_videotoolbox
 profile:H264_VIDEOTOOLBOX_PROFILE = '0'
 level:H264_VIDEOTOOLBOX_LEVEL = '0'
 coder:H264_VIDEOTOOLBOX_CODER = '0'
 a53cc:bool = True
 constant_bit_rate:bool = False
 allow_sw:bool = False
 require_sw:bool = False
 realtime:bool = False
 frames_before:bool = False
 frames_after:bool = False
 prio_speed:bool = 'auto' 
 ...


HEVC_VIDEOTOOLBOX_PROFILE = Literal['main', 'main10']

@dataclass
class hevc_videotoolbox(): # hevc_videotoolbox
 profile:HEVC_VIDEOTOOLBOX_PROFILE = '0'
 alpha_quality:float = '0'
 constant_bit_rate:bool = False
 allow_sw:bool = False
 require_sw:bool = False
 realtime:bool = False
 frames_before:bool = False
 frames_after:bool = False
 prio_speed:bool = 'auto' 
 ...


PRORES_VIDEOTOOLBOX_PROFILE = Literal['auto', 'proxy', 'lt', 'standard', 'hq', '4444', 'xq']

@dataclass
class prores_videotoolbox(): # prores_videotoolbox
 profile:PRORES_VIDEOTOOLBOX_PROFILE = 'auto'
 allow_sw:bool = False
 require_sw:bool = False
 realtime:bool = False
 frames_before:bool = False
 frames_after:bool = False
 prio_speed:bool = 'auto' 
 ...


EXR_APPLY_TRC = Literal['bt709', 'gamma', 'gamma22', 'gamma28', 'smpte170m', 'smpte240m', 'linear', 'log', 'log_sqrt', 'iec61966_2_4', 'bt1361', 'iec61966_2_1', 'bt2020_10bit', 'bt2020_12bit', 'smpte2084', 'smpte428_1']

@dataclass
class EXR(): # EXR
 layer:str = ""
 part:int = 0
 gamma:float = '1'
 apply_trc:EXR_APPLY_TRC = 'gamma' 
 ...




@dataclass
class FIC_decoder(): # FIC decoder
 skip_cursor:bool = False 
 ...




@dataclass
class FITS_decoder(): # FITS decoder
 blank_value:int = 0 
 ...




@dataclass
class frwu_Decoder(): # frwu Decoder
 change_field_order:bool = False 
 ...




@dataclass
class gif_decoder(): # gif decoder
 trans_color:int = 16777215 
 ...




@dataclass
class H264_Decoder(): # H264 Decoder
 is_avc:bool = False
 nal_length_size:int = 0
 enable_er:bool = 'auto'
 x264_build:int = -1 
 ...




@dataclass
class HEVC_decoder(): # HEVC decoder
 apply_defdispwin:bool = False
 strict_displaywin:bool = dataclasses_field(default=False, metadata='strict-displaywin') 
 ...




@dataclass
class jpeg2000(): # jpeg2000
 lowres:int = 0 
 ...




@dataclass
class MJPEG_decoder(): # MJPEG decoder
 extern_huff:bool = False 
 ...




@dataclass
class MPEG4_Video_Decoder(): # MPEG4 Video Decoder 
 ...




@dataclass
class photocd(): # photocd
 lowres:int = 0 
 ...




@dataclass
class rasc_decoder(): # rasc decoder
 skip_cursor:bool = False 
 ...




@dataclass
class rawdec(): # rawdec
 top:bool = 'auto' 
 ...


SMPTE_302M_DECODER_NON_PCM_MODE = Literal['copy', 'drop', 'decode_copy', 'decode_drop']

@dataclass
class SMPTE_302M_Decoder(): # SMPTE 302M Decoder
 non_pcm_mode:SMPTE_302M_DECODER_NON_PCM_MODE = 'decode_drop' 
 ...




@dataclass
class TIFF_decoder(): # TIFF decoder
 subimage:bool = False
 thumbnail:bool = False
 page:int = 0 
 ...




@dataclass
class V210_Decoder(): # V210 Decoder
 custom_stride:int = 0 
 ...


AAC_DECODER_DUAL_MONO_MODE = Literal['auto', 'main', 'sub', 'both']
AAC_DECODER_CHANNEL_ORDER = Literal['default', 'coded']

@dataclass
class AAC_decoder(): # AAC decoder
 dual_mono_mode:AAC_DECODER_DUAL_MONO_MODE = 'auto'
 channel_order:AAC_DECODER_CHANNEL_ORDER = 'default' 
 ...




@dataclass
class _E__AC3_decoder(): # (E-)AC3 decoder
 cons_noisegen:bool = False
 drc_scale:float = '1'
 heavy_compr:bool = False
 target_level:int = 0
 downmix:CHANNEL_LAYOUTS = None 
 ...




@dataclass
class Fixed_Point_AC_3_Decoder(): # Fixed-Point AC-3 Decoder
 cons_noisegen:bool = False
 drc_scale:float = '1'
 heavy_compr:bool = False
 downmix:CHANNEL_LAYOUTS = None 
 ...




@dataclass
class alac(): # alac
 extra_bits_bug:bool = False 
 ...


APE_DECODER_MAX_SAMPLES = Literal['all']

@dataclass
class APE_decoder(): # APE decoder
 max_samples:APE_DECODER_MAX_SAMPLES = '4608' 
 ...


DCA_DECODER_CHANNEL_ORDER = Literal['default', 'coded']

@dataclass
class DCA_decoder(): # DCA decoder
 core_only:bool = False
 channel_order:DCA_DECODER_CHANNEL_ORDER = 'default'
 downmix:CHANNEL_LAYOUTS = None 
 ...


DOLBY_E_DECODER_CHANNEL_ORDER = Literal['default', 'coded']

@dataclass
class Dolby_E_decoder(): # Dolby E decoder
 channel_order:DOLBY_E_DECODER_CHANNEL_ORDER = 'default' 
 ...




@dataclass
class evrc(): # evrc
 postfilter:bool = True 
 ...




@dataclass
class FLAC_decoder(): # FLAC decoder
 use_buggy_lpc:bool = False 
 ...




@dataclass
class G_723_1_decoder(): # G.723.1 decoder
 postfilter:bool = True 
 ...




@dataclass
class MLP_decoder(): # MLP decoder
 downmix:CHANNEL_LAYOUTS = None 
 ...




@dataclass
class Opus_Decoder(): # Opus Decoder
 apply_phase_inv:bool = True 
 ...




@dataclass
class TrueHD_decoder(): # TrueHD decoder
 downmix:CHANNEL_LAYOUTS = None 
 ...




@dataclass
class TTA_Decoder(): # TTA Decoder
 password:str = None 
 ...




@dataclass
class g722_decoder(): # g722 decoder
 bits_per_codeword:int = 8 
 ...


CLOSED_CAPTION_DECODER_DATA_FIELD = Literal['auto', 'first', 'second']

@dataclass
class Closed_caption_Decoder(): # Closed caption Decoder
 real_time:bool = False
 real_time_latency_msec:int = 200
 data_field:CLOSED_CAPTION_DECODER_DATA_FIELD = 'auto' 
 ...




@dataclass
class DVB_Sub_Decoder(): # DVB Sub Decoder
 compute_edt:bool = False
 compute_clut:bool = 'auto'
 dvb_substream:int = -1 
 ...




@dataclass
class dvdsubdec(): # dvdsubdec
 palette:str = None
 ifo_palette:str = None
 forced_subs_only:bool = False 
 ...




@dataclass
class MOV_text_decoder(): # MOV text decoder
 width:int = 0
 height:int = 0 
 ...




@dataclass
class PGS_subtitle_decoder(): # PGS subtitle decoder
 forced_subs_only:bool = False 
 ...




@dataclass
class text_vplayer_stl_pjs_subviewer1_decoder(): # text/vplayer/stl/pjs/subviewer1 decoder
 keep_ass_markup:bool = False 
 ...


LIBARIBB24_DECODER_DEFAULT_PROFILE = Literal['a', 'c']

@dataclass
class libaribb24_decoder(): # libaribb24 decoder
 aribb24_base_path:str = dataclasses_field(default=None, metadata='aribb24-base-path')
 aribb24_skip_ruby_text:bool = dataclasses_field(default=True, metadata='aribb24-skip-ruby-text')
 default_profile:LIBARIBB24_DECODER_DEFAULT_PROFILE = '-99' 
 ...




@dataclass
class libdav1d_decoder(): # libdav1d decoder
 tilethreads:int = 0
 framethreads:int = 0
 max_frame_delay:int = 0
 filmgrain:bool = 'auto'
 oppoint:int = -1
 alllayers:bool = False 
 ...




@dataclass
class libopusdec(): # libopusdec
 apply_phase_inv:bool = True 
 ...




@dataclass
class AV1_decoder(): # AV1 decoder
 operating_point:int = 0 
 ...


AVFORMATCONTEXT_AVIOFLAGS = Literal['direct']
AVFORMATCONTEXT_FFLAGS = Literal['flush_packets', 'ignidx', 'genpts', 'nofillin', 'noparse', 'igndts', 'discardcorrupt', 'sortdts', 'fastseek', 'nobuffer', 'bitexact', 'shortest', 'autobsf']
AVFORMATCONTEXT_FDEBUG = Literal['ts']
AVFORMATCONTEXT_F_ERR_DETECT = Literal['crccheck', 'bitstream', 'buffer', 'explode', 'ignore_err', 'careful', 'compliant', 'aggressive']
AVFORMATCONTEXT_F_STRICT = Literal['very', 'strict', 'normal', 'unofficial', 'experimental']
AVFORMATCONTEXT_AVOID_NEGATIVE_TS = Literal['auto', 'disabled', 'make_non_negative', 'make_zero']

@dataclass
class AVFormatContext(): # AVFormatContext
 avioflags:AVFORMATCONTEXT_AVIOFLAGS = '0'
 probesize:int = 5000000
 formatprobesize:int = 1048576
 packetsize:int = 0
 fflags:AVFORMATCONTEXT_FFLAGS = 'autobsf'
 seek2any:bool = False
 analyzeduration:int = 0
 cryptokey:str = None
 indexmem:int = 1048576
 rtbufsize:int = 3041280
 fdebug:AVFORMATCONTEXT_FDEBUG = '0'
 max_delay:int = -1
 start_time_realtime:int = 'I64_MIN'
 fpsprobesize:int = -1
 audio_preload:int = 0
 chunk_duration:int = 0
 chunk_size:int = 0
 f_err_detect:AVFORMATCONTEXT_F_ERR_DETECT = 'crccheck'
 err_detect:AVFORMATCONTEXT_F_ERR_DETECT = 'crccheck'
 use_wallclock_as_timestamps:bool = False
 skip_initial_bytes:int = 0
 correct_ts_overflow:bool = True
 flush_packets:int = -1
 metadata_header_padding:int = -1
 output_ts_offset:str = '0'
 max_interleave_delta:int = 10000000
 f_strict:AVFORMATCONTEXT_F_STRICT = 'normal'
 strict:AVFORMATCONTEXT_F_STRICT = 'normal'
 max_ts_probe:int = 50
 avoid_negative_ts:AVFORMATCONTEXT_AVOID_NEGATIVE_TS = 'auto'
 dump_separator:str = ", "
 codec_whitelist:str = None
 format_whitelist:str = None
 protocol_whitelist:str = None
 protocol_blacklist:str = None
 max_streams:int = 1000
 skip_estimate_duration_from_pts:bool = False
 max_probe_packets:int = 2500 
 ...




@dataclass
class AVIOContext(): # AVIOContext
 protocol_whitelist:str = None 
 ...




@dataclass
class URLContext(): # URLContext
 protocol_whitelist:str = None
 protocol_blacklist:str = None
 rw_timeout:int = 0 
 ...




@dataclass
class Async(): # Async 
 ...




@dataclass
class bluray(): # bluray
 playlist:int = -1
 angle:int = 0
 chapter:int = 1 
 ...




@dataclass
class cache(): # cache
 read_ahead_limit:int = 65536 
 ...




@dataclass
class crypto(): # crypto
 key:str = None
 iv:str = None
 decryption_key:str = None
 decryption_iv:str = None
 encryption_key:str = None
 encryption_iv:str = None 
 ...




@dataclass
class fd(): # fd
 blocksize:int = 'INT_MAX'
 fd:int = -1 
 ...




@dataclass
class ffrtmphttp(): # ffrtmphttp
 ffrtmphttp_tls:bool = False 
 ...




@dataclass
class file(): # file
 truncate:bool = True
 blocksize:int = 'INT_MAX'
 follow:int = 0
 seekable:int = -1 
 ...




@dataclass
class ftp(): # ftp
 timeout:int = -1
 ftp_write_seekable:bool = dataclasses_field(default=False, metadata='ftp-write-seekable')
 ftp_anonymous_password:str = dataclasses_field(default=None, metadata='ftp-anonymous-password')
 ftp_user:str = dataclasses_field(default=None, metadata='ftp-user')
 ftp_password:str = dataclasses_field(default=None, metadata='ftp-password') 
 ...


HTTP_AUTH_TYPE = Literal['none', 'basic']

@dataclass
class http(): # http
 seekable:bool = 'auto'
 chunked_post:bool = True
 http_proxy:str = None
 headers:str = None
 content_type:str = None
 user_agent:str = "Lavf/60.3.100"
 referer:str = None
 multiple_requests:bool = False
 post_data:str = None
 cookies:str = None
 icy:bool = True
 auth_type:HTTP_AUTH_TYPE = 'none'
 send_expect_100:bool = 'auto'
 location:str = None
 offset:int = 0
 end_offset:int = 0
 method:str = None
 reconnect:bool = False
 reconnect_at_eof:bool = False
 reconnect_on_network_error:bool = False
 reconnect_on_http_error:str = None
 reconnect_streamed:bool = False
 reconnect_delay_max:int = 120
 listen:int = 0
 resource:str = None
 reply_code:int = 200
 short_seek_size:int = 0 
 ...


HTTPS_AUTH_TYPE = Literal['none', 'basic']

@dataclass
class https(): # https
 seekable:bool = 'auto'
 chunked_post:bool = True
 http_proxy:str = None
 headers:str = None
 content_type:str = None
 user_agent:str = "Lavf/60.3.100"
 referer:str = None
 multiple_requests:bool = False
 post_data:str = None
 cookies:str = None
 icy:bool = True
 auth_type:HTTPS_AUTH_TYPE = 'none'
 send_expect_100:bool = 'auto'
 location:str = None
 offset:int = 0
 end_offset:int = 0
 method:str = None
 reconnect:bool = False
 reconnect_at_eof:bool = False
 reconnect_on_network_error:bool = False
 reconnect_on_http_error:str = None
 reconnect_streamed:bool = False
 reconnect_delay_max:int = 120
 listen:int = 0
 resource:str = None
 reply_code:int = 200
 short_seek_size:int = 0 
 ...




@dataclass
class icecast(): # icecast
 ice_genre:str = None
 ice_name:str = None
 ice_description:str = None
 ice_url:str = None
 ice_public:bool = False
 user_agent:str = None
 password:str = None
 content_type:str = None
 legacy_icecast:bool = False
 tls:bool = False 
 ...




@dataclass
class pipe(): # pipe
 blocksize:int = 'INT_MAX'
 fd:int = -1 
 ...




@dataclass
class prompeg(): # prompeg
 ttl:int = -1
 l:int = 5
 d:int = 5 
 ...


RTMP_RTMP_LIVE = Literal['any', 'live', 'recorded']

@dataclass
class rtmp(): # rtmp
 rtmp_app:str = None
 rtmp_buffer:int = 3000
 rtmp_conn:str = None
 rtmp_flashver:str = None
 rtmp_flush_interval:int = 10
 rtmp_live:RTMP_RTMP_LIVE = 'any'
 rtmp_pageurl:str = None
 rtmp_playpath:str = None
 rtmp_subscribe:str = None
 rtmp_swfhash:str = None
 rtmp_swfsize:int = 0
 rtmp_swfurl:str = None
 rtmp_swfverify:str = None
 rtmp_tcurl:str = None
 rtmp_listen:int = 0
 listen:int = 0
 tcp_nodelay:int = 0
 timeout:int = -1 
 ...


RTMPS_RTMP_LIVE = Literal['any', 'live', 'recorded']

@dataclass
class rtmps(): # rtmps
 rtmp_app:str = None
 rtmp_buffer:int = 3000
 rtmp_conn:str = None
 rtmp_flashver:str = None
 rtmp_flush_interval:int = 10
 rtmp_live:RTMPS_RTMP_LIVE = 'any'
 rtmp_pageurl:str = None
 rtmp_playpath:str = None
 rtmp_subscribe:str = None
 rtmp_swfhash:str = None
 rtmp_swfsize:int = 0
 rtmp_swfurl:str = None
 rtmp_swfverify:str = None
 rtmp_tcurl:str = None
 rtmp_listen:int = 0
 listen:int = 0
 tcp_nodelay:int = 0
 timeout:int = -1 
 ...


RTMPT_RTMP_LIVE = Literal['any', 'live', 'recorded']

@dataclass
class rtmpt(): # rtmpt
 rtmp_app:str = None
 rtmp_buffer:int = 3000
 rtmp_conn:str = None
 rtmp_flashver:str = None
 rtmp_flush_interval:int = 10
 rtmp_live:RTMPT_RTMP_LIVE = 'any'
 rtmp_pageurl:str = None
 rtmp_playpath:str = None
 rtmp_subscribe:str = None
 rtmp_swfhash:str = None
 rtmp_swfsize:int = 0
 rtmp_swfurl:str = None
 rtmp_swfverify:str = None
 rtmp_tcurl:str = None
 rtmp_listen:int = 0
 listen:int = 0
 tcp_nodelay:int = 0
 timeout:int = -1 
 ...


RTMPTS_RTMP_LIVE = Literal['any', 'live', 'recorded']

@dataclass
class rtmpts(): # rtmpts
 rtmp_app:str = None
 rtmp_buffer:int = 3000
 rtmp_conn:str = None
 rtmp_flashver:str = None
 rtmp_flush_interval:int = 10
 rtmp_live:RTMPTS_RTMP_LIVE = 'any'
 rtmp_pageurl:str = None
 rtmp_playpath:str = None
 rtmp_subscribe:str = None
 rtmp_swfhash:str = None
 rtmp_swfsize:int = 0
 rtmp_swfurl:str = None
 rtmp_swfverify:str = None
 rtmp_tcurl:str = None
 rtmp_listen:int = 0
 listen:int = 0
 tcp_nodelay:int = 0
 timeout:int = -1 
 ...




@dataclass
class rtp(): # rtp
 ttl:int = -1
 buffer_size:int = -1
 rtcp_port:int = -1
 local_rtpport:int = -1
 local_rtcpport:int = -1
 connect:bool = False
 write_to_source:bool = False
 pkt_size:int = -1
 dscp:int = -1
 timeout:int = -1
 sources:str = None
 block:str = None
 fec:str = None
 localaddr:str = None 
 ...




@dataclass
class srtp(): # srtp
 srtp_out_suite:str = None
 srtp_out_params:str = None
 srtp_in_suite:str = None
 srtp_in_params:str = None 
 ...




@dataclass
class subfile(): # subfile
 start:int = 0
 end:int = 0 
 ...




@dataclass
class tee(): # tee 
 ...




@dataclass
class tcp(): # tcp
 listen:int = 0
 timeout:int = -1
 listen_timeout:int = -1
 send_buffer_size:int = -1
 recv_buffer_size:int = -1
 tcp_nodelay:bool = False
 tcp_mss:int = -1 
 ...




@dataclass
class tls(): # tls
 ca_file:str = None
 cafile:str = None
 tls_verify:int = 0
 cert_file:str = None
 key_file:str = None
 listen:int = 0
 verifyhost:str = None
 http_proxy:str = None 
 ...




@dataclass
class udp(): # udp
 buffer_size:int = -1
 bitrate:int = 0
 burst_bits:int = 0
 localport:int = -1
 local_port:int = -1
 localaddr:str = None
 udplite_coverage:int = 0
 pkt_size:int = 1472
 reuse:bool = 'auto'
 reuse_socket:bool = 'auto'
 broadcast:bool = False
 ttl:int = 16
 connect:bool = False
 fifo_size:int = 28672
 overrun_nonfatal:bool = False
 timeout:int = 0
 sources:str = None
 block:str = None 
 ...




@dataclass
class udplite(): # udplite
 buffer_size:int = -1
 bitrate:int = 0
 burst_bits:int = 0
 localport:int = -1
 local_port:int = -1
 localaddr:str = None
 udplite_coverage:int = 0
 pkt_size:int = 1472
 reuse:bool = 'auto'
 reuse_socket:bool = 'auto'
 broadcast:bool = False
 ttl:int = 16
 connect:bool = False
 fifo_size:int = 28672
 overrun_nonfatal:bool = False
 timeout:int = 0
 sources:str = None
 block:str = None 
 ...


UNIX_TYPE = Literal['stream', 'datagram', 'seqpacket']

@dataclass
class unix(): # unix
 listen:bool = False
 timeout:int = -1
 type:UNIX_TYPE = 'stream' 
 ...


LIBRIST_RIST_PROFILE = Literal['simple', 'main', 'advanced']

@dataclass
class librist(): # librist
 rist_profile:LIBRIST_RIST_PROFILE = 'main'
 buffer_size:int = 0
 fifo_size:int = 8192
 overrun_nonfatal:bool = False
 pkt_size:int = 1316
 log_level:int = 6
 secret:str = None
 encryption:int = 0 
 ...


LIBSRT_PKT_SIZE = Literal['ts_size', 'max_size']
LIBSRT_MODE = Literal['caller', 'listener', 'rendezvous']
LIBSRT_TRANSTYPE = Literal['live', 'file']

@dataclass
class libsrt(): # libsrt
 timeout:int = -1
 listen_timeout:int = -1
 send_buffer_size:int = -1
 recv_buffer_size:int = -1
 pkt_size:LIBSRT_PKT_SIZE = '-1'
 payload_size:LIBSRT_PKT_SIZE = '-1'
 maxbw:int = -1
 pbkeylen:int = -1
 passphrase:str = None
 enforced_encryption:bool = 'auto'
 kmrefreshrate:int = -1
 kmpreannounce:int = -1
 snddropdelay:int = -2
 mss:int = -1
 ffs:int = -1
 ipttl:int = -1
 iptos:int = -1
 inputbw:int = -1
 oheadbw:int = -1
 latency:int = -1
 tsbpddelay:int = -1
 rcvlatency:int = -1
 peerlatency:int = -1
 tlpktdrop:bool = 'auto'
 nakreport:bool = 'auto'
 connect_timeout:int = -1
 mode:LIBSRT_MODE = 'caller'
 sndbuf:int = -1
 rcvbuf:int = -1
 lossmaxttl:int = -1
 minversion:int = -1
 streamid:str = None
 srt_streamid:str = None
 smoother:str = None
 messageapi:bool = 'auto'
 transtype:LIBSRT_TRANSTYPE = '2'
 linger:int = -1
 tsbpd:bool = 'auto' 
 ...




@dataclass
class zmq(): # zmq
 pkt_size:int = 131072 
 ...




@dataclass
class IPFS_Gateway(): # IPFS Gateway
 gateway:str = None 
 ...




@dataclass
class ADTS_muxer(): # ADTS muxer
 write_id3v2:bool = False
 write_apetag:bool = False
 write_mpeg2:bool = False 
 ...




@dataclass
class AIFF_muxer(): # AIFF muxer
 write_id3v2:bool = False
 id3v2_version:int = 4 
 ...


ALP_TYPE = Literal['auto', 'tun', 'pcm']

@dataclass
class alp(): # alp
 type:ALP_TYPE = 'auto' 
 ...




@dataclass
class APNG_muxer(): # APNG muxer
 plays:int = 1
 final_delay:float|str = '0/1' 
 ...




@dataclass
class argo_asf_muxer(): # argo_asf_muxer
 version_major:int = 2
 version_minor:int = 1
 name:str = None 
 ...




@dataclass
class argo_cvg_muxer(): # argo_cvg_muxer
 skip_rate_check:bool = False
 loop:bool = False
 reverb:bool = True 
 ...




@dataclass
class ASF__stream__muxer(): # ASF (stream) muxer
 packet_size:int = 3200 
 ...




@dataclass
class ass_muxer(): # ass muxer
 ignore_readorder:bool = False 
 ...




@dataclass
class AST_muxer(): # AST muxer
 loopstart:int = -1
 loopend:int = 0 
 ...




@dataclass
class AVI_muxer(): # AVI muxer
 reserve_index_space:int = 0
 write_channel_mask:bool = True
 flipped_raw_rgb:bool = False 
 ...




@dataclass
class avif_muxer(): # avif muxer
 movie_timescale:int = 1000
 loop:int = 0 
 ...


DASH_MUXER_FRAG_TYPE = Literal['none', 'every_frame', 'duration', 'pframes']
DASH_MUXER_DASH_SEGMENT_TYPE = Literal['auto', 'mp4', 'webm']
DASH_MUXER_MPD_PROFILE = Literal['dash', 'dvb_dash']

@dataclass
class dash_muxer(): # dash muxer
 adaptation_sets:str = None
 window_size:int = 0
 extra_window_size:int = 5
 seg_duration:str = '5'
 frag_duration:str = '0'
 frag_type:DASH_MUXER_FRAG_TYPE = 'none'
 remove_at_exit:bool = False
 use_template:bool = True
 use_timeline:bool = True
 single_file:bool = False
 single_file_name:str = None
 init_seg_name:str = "init-stream$RepresentationID$.$ext$"
 media_seg_name:str = "chunk-stream$RepresentationID$-$Number%05d$.$ext$"
 utc_timing_url:str = None
 method:str = None
 http_user_agent:str = None
 http_persistent:bool = False
 hls_playlist:bool = False
 hls_master_name:str = "master.m3u8"
 streaming:bool = False
 timeout:str = '-0.000001'
 index_correction:bool = False
 format_options:dict = None
 global_sidx:bool = False
 dash_segment_type:DASH_MUXER_DASH_SEGMENT_TYPE = 'auto'
 ignore_io_errors:bool = False
 lhls:bool = False
 ldash:bool = False
 master_m3u8_publish_rate:int = 0
 write_prft:bool = 'auto'
 mpd_profile:DASH_MUXER_MPD_PROFILE = 'dash'
 http_opts:dict = None
 target_latency:str = '0'
 min_playback_rate:float|str = '1/1'
 max_playback_rate:float|str = '1/1'
 update_period:int = 0 
 ...


MOV_MP4_TGP_PSP_TG2_IPOD_ISMV_F4V_MUXER_MOVFLAGS = Literal['rtphint', 'empty_moov', 'frag_keyframe', 'frag_every_frame', 'separate_moof', 'frag_custom', 'isml', 'faststart', 'omit_tfhd_offset', 'disable_chpl', 'default_base_moof', 'dash', 'cmaf', 'frag_discont', 'delay_moov', 'global_sidx', 'skip_sidx', 'write_colr', 'prefer_icc', 'write_gama', 'use_metadata_tags', 'skip_trailer', 'negative_cts_offsets']
MOV_MP4_TGP_PSP_TG2_IPOD_ISMV_F4V_MUXER_RTPFLAGS = Literal['latm', 'rfc2190', 'skip_rtcp', 'h264_mode0', 'send_bye']
MOV_MP4_TGP_PSP_TG2_IPOD_ISMV_F4V_MUXER_WRITE_PRFT = Literal['wallclock', 'pts']

@dataclass
class mov_mp4_tgp_psp_tg2_ipod_ismv_f4v_muxer(): # mov/mp4/tgp/psp/tg2/ipod/ismv/f4v muxer
 movflags:MOV_MP4_TGP_PSP_TG2_IPOD_ISMV_F4V_MUXER_MOVFLAGS = '0'
 moov_size:int = 0
 rtpflags:MOV_MP4_TGP_PSP_TG2_IPOD_ISMV_F4V_MUXER_RTPFLAGS = '0'
 skip_iods:bool = True
 iods_audio_profile:int = -1
 iods_video_profile:int = -1
 frag_duration:int = 0
 min_frag_duration:int = 0
 frag_size:int = 0
 ism_lookahead:int = 0
 video_track_timescale:int = 0
 brand:str = None
 use_editlist:bool = 'auto'
 fragment_index:int = 1
 mov_gamma:float = '0'
 frag_interleave:int = 0
 encryption_scheme:str = None
 encryption_key:str = None
 encryption_kid:str = None
 use_stream_ids_as_track_ids:bool = False
 write_btrt:bool = 'auto'
 write_tmcd:bool = 'auto'
 write_prft:MOV_MP4_TGP_PSP_TG2_IPOD_ISMV_F4V_MUXER_WRITE_PRFT = '0'
 empty_hdlr_name:bool = False
 movie_timescale:int = 1000 
 ...




@dataclass
class Fifo_muxer(): # Fifo muxer
 fifo_format:str = None
 queue_size:int = 60
 format_opts:dict = None
 drop_pkts_on_overflow:bool = False
 restart_with_keyframe:bool = False
 attempt_recovery:bool = False
 max_recovery_attempts:int = 0
 recovery_wait_time:str = '5'
 recovery_wait_streamtime:bool = False
 recover_any_error:bool = False
 timeshift:str = '0' 
 ...




@dataclass
class Fifo_test_muxer(): # Fifo test muxer
 write_header_ret:int = 0
 write_trailer_ret:int = 0
 print_deinit_summary:bool = True 
 ...




@dataclass
class flac_muxer(): # flac muxer
 write_header:bool = True 
 ...


FLV_MUXER_FLVFLAGS = Literal['aac_seq_header_detect', 'no_sequence_end', 'no_metadata', 'no_duration_filesize', 'add_keyframe_index']

@dataclass
class flv_muxer(): # flv muxer
 flvflags:FLV_MUXER_FLVFLAGS = '0' 
 ...




@dataclass
class frame_hash_muxer(): # frame hash muxer
 hash:str = "sha256"
 format_version:int = 2 
 ...




@dataclass
class frame_MD5_muxer(): # frame MD5 muxer
 hash:str = "md5"
 format_version:int = 2 
 ...




@dataclass
class GIF_muxer(): # GIF muxer
 loop:int = 0
 final_delay:int = -1 
 ...




@dataclass
class _stream__hash_muxer(): # (stream) hash muxer
 hash:str = "sha256" 
 ...




@dataclass
class HDS_muxer(): # HDS muxer
 window_size:int = 0
 extra_window_size:int = 5
 min_frag_duration:int = 10000000
 remove_at_exit:bool = False 
 ...


HLS_MUXER_HLS_SEGMENT_TYPE = Literal['mpegts', 'fmp4']
HLS_MUXER_HLS_FLAGS = Literal['single_file', 'temp_file', 'delete_segments', 'round_durations', 'discont_start', 'omit_endlist', 'split_by_time', 'append_list', 'program_date_time', 'second_level_segment_index', 'second_level_segment_duration', 'second_level_segment_size', 'periodic_rekey', 'independent_segments', 'iframes_only']
HLS_MUXER_HLS_PLAYLIST_TYPE = Literal['event', 'vod']
HLS_MUXER_HLS_START_NUMBER_SOURCE = Literal['generic', 'epoch', 'epoch_us', 'datetime']

@dataclass
class hls_muxer(): # hls muxer
 start_number:int = 0
 hls_time:str = '2'
 hls_init_time:str = '0'
 hls_list_size:int = 5
 hls_delete_threshold:int = 1
 hls_vtt_options:str = None
 hls_allow_cache:int = -1
 hls_base_url:str = None
 hls_segment_filename:str = None
 hls_segment_options:dict = None
 hls_segment_size:int = 0
 hls_key_info_file:str = None
 hls_enc:bool = False
 hls_enc_key:str = None
 hls_enc_key_url:str = None
 hls_enc_iv:str = None
 hls_subtitle_path:str = None
 hls_segment_type:HLS_MUXER_HLS_SEGMENT_TYPE = 'mpegts'
 hls_fmp4_init_filename:str = "init.mp4"
 hls_fmp4_init_resend:bool = False
 hls_flags:HLS_MUXER_HLS_FLAGS = '0'
 strftime:bool = False
 strftime_mkdir:bool = False
 hls_playlist_type:HLS_MUXER_HLS_PLAYLIST_TYPE = '0'
 method:str = ': PUT'
 hls_start_number_source:HLS_MUXER_HLS_START_NUMBER_SOURCE = 'generic'
 http_user_agent:str = None
 var_stream_map:str = None
 cc_stream_map:str = None
 master_pl_name:str = None
 master_pl_publish_rate:int = 0
 http_persistent:bool = False
 timeout:str = '-0.000001'
 ignore_io_errors:bool = False
 headers:str = None 
 ...




@dataclass
class image2_muxer(): # image2 muxer
 update:bool = False
 start_number:int = 1
 strftime:bool = False
 frame_pts:bool = False
 atomic_writing:bool = False
 protocol_opts:dict = None 
 ...




@dataclass
class LATM_LOAS_muxer(): # LATM/LOAS muxer
 smc_interval:int = dataclasses_field(default=20, metadata='smc-interval') 
 ...




@dataclass
class MD5_muxer(): # MD5 muxer
 hash:str = "md5" 
 ...


MATROSKA_WEBM_MUXER_DEFAULT_MODE = Literal['infer', 'infer_no_subs', 'passthrough']

@dataclass
class matroska_webm_muxer(): # matroska/webm muxer
 reserve_index_space:int = 0
 cues_to_front:bool = False
 cluster_size_limit:int = -1
 cluster_time_limit:int = -1
 dash:bool = False
 dash_track_number:int = 1
 live:bool = False
 allow_raw_vfw:bool = False
 flipped_raw_rgb:bool = False
 write_crc32:bool = True
 default_mode:MATROSKA_WEBM_MUXER_DEFAULT_MODE = 'passthrough' 
 ...




@dataclass
class MP3_muxer(): # MP3 muxer
 id3v2_version:int = 4
 write_id3v1:bool = False
 write_xing:bool = True 
 ...




@dataclass
class mpeg__s_vcd_vob_dvd_muxer(): # mpeg/(s)vcd/vob/dvd muxer
 muxrate:int = 0
 preload:int = 500000 
 ...


MPEGTS_MUXER_MPEGTS_SERVICE_TYPE = Literal['digital_tv', 'digital_radio', 'teletext', 'advanced_codec_digital_radio', 'mpeg2_digital_hdtv', 'advanced_codec_digital_sdtv', 'advanced_codec_digital_hdtv', 'hevc_digital_hdtv']
MPEGTS_MUXER_MPEGTS_FLAGS = Literal['resend_headers', 'latm', 'pat_pmt_at_frames', 'system_b', 'initial_discontinuity', 'nit', 'omit_rai']

@dataclass
class MPEGTS_muxer(): # MPEGTS muxer
 mpegts_transport_stream_id:int = 1
 mpegts_original_network_id:int = 65281
 mpegts_service_id:int = 1
 mpegts_service_type:MPEGTS_MUXER_MPEGTS_SERVICE_TYPE = 'digital_tv'
 mpegts_pmt_start_pid:int = 4096
 mpegts_start_pid:int = 256
 mpegts_m2ts_mode:bool = 'auto'
 muxrate:int = 1
 pes_payload_size:int = 2930
 mpegts_flags:MPEGTS_MUXER_MPEGTS_FLAGS = '0'
 mpegts_copyts:bool = 'auto'
 tables_version:int = 0
 omit_video_pes_length:bool = True
 pcr_period:int = -1
 pat_period:str = '0.1'
 sdt_period:str = '0.5'
 nit_period:str = '0.5' 
 ...




@dataclass
class mpjpeg_muxer(): # mpjpeg_muxer
 boundary_tag:str = "ffmpeg" 
 ...


MXF_MUXER_SIGNAL_STANDARD = Literal['bt601', 'bt1358', 'smpte347m', 'smpte274m', 'smpte296m', 'smpte349m', 'smpte428']

@dataclass
class MXF_muxer(): # MXF muxer
 signal_standard:MXF_MUXER_SIGNAL_STANDARD = '-1'
 store_user_comments:bool = True 
 ...


MXF_D10_MUXER_SIGNAL_STANDARD = Literal['bt601', 'bt1358', 'smpte347m', 'smpte274m', 'smpte296m', 'smpte349m', 'smpte428']

@dataclass
class MXF_D10_muxer(): # MXF-D10 muxer
 d10_channelcount:int = -1
 signal_standard:MXF_D10_MUXER_SIGNAL_STANDARD = '-1'
 store_user_comments:bool = False 
 ...


MXF_OPATOM_MUXER_SIGNAL_STANDARD = Literal['bt601', 'bt1358', 'smpte347m', 'smpte274m', 'smpte296m', 'smpte349m', 'smpte428']

@dataclass
class MXF_OPAtom_muxer(): # MXF-OPAtom muxer
 mxf_audio_edit_rate:float|str = '25/1'
 signal_standard:MXF_OPATOM_MUXER_SIGNAL_STANDARD = '-1'
 store_user_comments:bool = True 
 ...


NUTENC_SYNCPOINTS = Literal['default', 'none', 'timestamped']

@dataclass
class nutenc(): # nutenc
 syncpoints:NUTENC_SYNCPOINTS = '0'
 write_index:bool = True 
 ...




@dataclass
class Ogg__audio_video_Speex_Opus__muxer(): # Ogg (audio/video/Speex/Opus) muxer
 serial_offset:int = 0
 oggpagesize:int = 0
 pagesize:int = 0
 page_duration:int = 1000000 
 ...


RTP_MUXER_RTPFLAGS = Literal['latm', 'rfc2190', 'skip_rtcp', 'h264_mode0', 'send_bye']

@dataclass
class RTP_muxer(): # RTP muxer
 rtpflags:RTP_MUXER_RTPFLAGS = '0'
 payload_type:int = -1
 ssrc:int = 0
 cname:str = None
 seq:int = -1 
 ...




@dataclass
class rtp_mpegts_muxer(): # rtp_mpegts muxer
 mpegts_muxer_options:dict = None
 rtp_muxer_options:dict = None 
 ...


RTSP_MUXER_RTPFLAGS = Literal['latm', 'rfc2190', 'skip_rtcp', 'h264_mode0', 'send_bye']
RTSP_MUXER_RTSP_TRANSPORT = Literal['udp', 'tcp', 'udp_multicast', 'http', 'https']
RTSP_MUXER_RTSP_FLAGS = Literal['filter_src', 'listen', 'prefer_tcp', 'satip_raw']
RTSP_MUXER_ALLOWED_MEDIA_TYPES = Literal['video', 'audio', 'data', 'subtitle']

@dataclass
class RTSP_muxer(): # RTSP muxer
 initial_pause:bool = False
 rtpflags:RTSP_MUXER_RTPFLAGS = '0'
 rtsp_transport:RTSP_MUXER_RTSP_TRANSPORT = '0'
 rtsp_flags:RTSP_MUXER_RTSP_FLAGS = '0'
 allowed_media_types:RTSP_MUXER_ALLOWED_MEDIA_TYPES = 'video+audio+data+subtitle'
 min_port:int = 5000
 max_port:int = 65000
 listen_timeout:int = -1
 timeout:int = 0
 reorder_queue_size:int = -1
 buffer_size:int = -1
 pkt_size:int = 1472
 user_agent:str = "Lavf60.3.100" 
 ...


_STREAM__SEGMENT_MUXER_SEGMENT_LIST_FLAGS = Literal['cache', 'live']
_STREAM__SEGMENT_MUXER_SEGMENT_LIST_TYPE = Literal['flat', 'csv', 'ext', 'ffconcat', 'm3u8', 'hls']

@dataclass
class _stream__segment_muxer(): # (stream) segment muxer
 reference_stream:str = "auto"
 segment_format:str = None
 segment_format_options:dict = None
 segment_list:str = None
 segment_header_filename:str = None
 segment_list_flags:_STREAM__SEGMENT_MUXER_SEGMENT_LIST_FLAGS = 'cache'
 segment_list_size:int = 0
 segment_list_type:_STREAM__SEGMENT_MUXER_SEGMENT_LIST_TYPE = '-1'
 segment_atclocktime:bool = False
 segment_clocktime_offset:str = '0'
 segment_clocktime_wrap_duration:str = 'INT64_MAX'
 segment_time:str = '2'
 segment_time_delta:str = '0'
 min_seg_duration:str = '0'
 segment_times:str = None
 segment_frames:str = None
 segment_wrap:int = 0
 segment_list_entry_prefix:str = None
 segment_start_number:int = 0
 segment_wrap_number:int = 0
 strftime:bool = False
 increment_tc:bool = False
 break_non_keyframes:bool = False
 individual_header_trailer:bool = True
 write_header_trailer:bool = True
 reset_timestamps:bool = False
 initial_offset:str = '0'
 write_empty_segments:bool = False 
 ...




@dataclass
class smooth_streaming_muxer(): # smooth streaming muxer
 window_size:int = 0
 extra_window_size:int = 5
 lookahead_count:int = 2
 min_frag_duration:int = 5000000
 remove_at_exit:bool = False 
 ...


SPDIF_SPDIF_FLAGS = Literal['be']

@dataclass
class spdif(): # spdif
 spdif_flags:SPDIF_SPDIF_FLAGS = '0'
 dtshd_rate:int = 0
 dtshd_fallback_time:int = 60 
 ...




@dataclass
class Tee_muxer(): # Tee muxer
 use_fifo:bool = False
 fifo_options:dict = None 
 ...


WAV_MUXER_WRITE_PEAK = Literal['off', 'on', 'only']
WAV_MUXER_RF64 = Literal['auto', 'always', 'never']

@dataclass
class WAV_muxer(): # WAV muxer
 write_bext:bool = False
 write_peak:WAV_MUXER_WRITE_PEAK = 'off'
 rf64:WAV_MUXER_RF64 = 'never'
 peak_block_size:int = 256
 peak_format:int = 2
 peak_ppv:int = 2 
 ...




@dataclass
class WebM_DASH_Manifest_muxer(): # WebM DASH Manifest muxer
 adaptation_sets:str = None
 live:bool = False
 chunk_start_index:int = 0
 chunk_duration_ms:int = 1000
 utc_timing_url:str = None
 time_shift_buffer_depth:float = '60'
 minimum_update_period:int = 0 
 ...




@dataclass
class WebM_Chunk_Muxer(): # WebM Chunk Muxer
 chunk_start_index:int = 0
 header:str = None
 audio_chunk_duration:int = 5000
 method:str = None 
 ...




@dataclass
class WebP_muxer(): # WebP muxer
 loop:int = 1 
 ...




@dataclass
class AudioToolbox(): # AudioToolbox
 list_devices:bool = False
 audio_device_index:int = -1 
 ...




@dataclass
class sdl2_outdev(): # sdl2 outdev
 window_title:str = None
 window_size:IMAGE_SIZES = None
 window_x:int = 805240832
 window_y:int = 805240832
 window_fullscreen:bool = False
 window_borderless:bool = False
 window_enable_quit:int = 1 
 ...




@dataclass
class aa(): # aa
 aa_fixed_key:str = None 
 ...




@dataclass
class generic_raw_demuxer(): # generic raw demuxer
 raw_packet_size:int = 1024 
 ...




@dataclass
class Artworx_Data_Format_demuxer(): # Artworx Data Format demuxer
 linespeed:int = 6000
 video_size:IMAGE_SIZES = None
 framerate:VIDEO_RATES = "25" 
 ...




@dataclass
class APNG_demuxer(): # APNG demuxer
 ignore_loop:bool = True
 max_fps:int = 0
 default_fps:int = 15 
 ...




@dataclass
class aptx__hd__demuxer(): # aptx (hd) demuxer
 sample_rate:int = 48000 
 ...




@dataclass
class aqtdec(): # aqtdec
 subfps:float|str = '25/1' 
 ...




@dataclass
class asf_demuxer(): # asf demuxer
 no_resync_search:bool = False
 export_xmp:bool = False 
 ...




@dataclass
class AV1_Annex_B_low_overhead_OBU_demuxer(): # AV1 Annex B/low overhead OBU demuxer
 framerate:VIDEO_RATES = "25" 
 ...




@dataclass
class avi(): # avi
 use_odml:bool = True 
 ...




@dataclass
class generic_raw_video_demuxer(): # generic raw video demuxer
 framerate:VIDEO_RATES = "25"
 raw_packet_size:int = 1024 
 ...




@dataclass
class Binary_text_demuxer(): # Binary text demuxer
 linespeed:int = 6000
 video_size:IMAGE_SIZES = None
 framerate:VIDEO_RATES = "25" 
 ...




@dataclass
class bitpacked_demuxer(): # bitpacked demuxer
 pixel_format:str = "yuv420p"
 video_size:IMAGE_SIZES = None
 framerate:VIDEO_RATES = "25" 
 ...




@dataclass
class CDXL_demuxer(): # CDXL demuxer
 sample_rate:int = 11025
 frame_rate:VIDEO_RATES = "15" 
 ...




@dataclass
class codec2_demuxer(): # codec2 demuxer
 frames_per_packet:int = 1 
 ...


CODEC2RAW_DEMUXER_MODE = Literal['3200', '2400', '1600', '1400', '1300', '1200', '700', '700B', '700C']

@dataclass
class codec2raw_demuxer(): # codec2raw demuxer
 mode:CODEC2RAW_DEMUXER_MODE = '-1'
 frames_per_packet:int = 1 
 ...




@dataclass
class concat_demuxer(): # concat demuxer
 safe:bool = True
 auto_convert:bool = True
 segment_time_metadata:bool = False 
 ...




@dataclass
class dash(): # dash
 allowed_extensions:str = "aac,m4a,m4s,m4v,mov,mp4,webm,ts"
 cenc_decryption_key:str = None 
 ...




@dataclass
class dfpwm_demuxer(): # dfpwm demuxer
 sample_rate:int = 48000
 channels:int = 1
 ch_layout:CHANNEL_LAYOUTS = None 
 ...




@dataclass
class ea_demuxer(): # ea demuxer
 merge_alpha:bool = False 
 ...




@dataclass
class FITS_demuxer(): # FITS demuxer
 framerate:VIDEO_RATES = "1" 
 ...




@dataclass
class _live__flv_kux_demuxer(): # (live) flv/kux demuxer
 flv_metadata:bool = False
 flv_full_metadata:bool = False
 flv_ignore_prevtag:bool = False
 missing_streams:int = 0 
 ...




@dataclass
class G_726_demuxer(): # G.726 demuxer
 code_size:int = 4
 sample_rate:int = 8000 
 ...




@dataclass
class g729_demuxer(): # g729 demuxer
 bit_rate:int = 8000 
 ...




@dataclass
class GIF_demuxer(): # GIF demuxer
 min_delay:int = 2
 max_gif_delay:int = 65535
 default_delay:int = 10
 ignore_loop:bool = True 
 ...




@dataclass
class gsm_demuxer(): # gsm demuxer
 sample_rate:int = 8000 
 ...




@dataclass
class hls_demuxer(): # hls demuxer
 live_start_index:int = -3
 prefer_x_start:bool = False
 allowed_extensions:str = "3gp,aac,avi,ac3,eac3,flac,mkv,m3u8,m4a,m4s,m4v,mpg,mov,mp2,mp3,mp4,mpeg,mpegts,ogg,ogv,oga,ts,vob,wav"
 max_reload:int = 1000
 m3u8_hold_counters:int = 1000
 http_persistent:bool = True
 http_multiple:bool = 'auto'
 http_seekable:bool = 'auto'
 seg_format_options:dict = None
 seg_max_retry:int = 0 
 ...




@dataclass
class iCE_Draw_File_demuxer(): # iCE Draw File demuxer
 linespeed:int = 6000
 video_size:IMAGE_SIZES = None
 framerate:VIDEO_RATES = "25" 
 ...


IMAGE2_DEMUXER_PATTERN_TYPE = Literal['glob_sequence', 'glob', 'sequence', 'none']
IMAGE2_DEMUXER_TS_FROM_FILE = Literal['none', 'sec', 'ns']

@dataclass
class image2_demuxer(): # image2 demuxer
 pattern_type:IMAGE2_DEMUXER_PATTERN_TYPE = '4'
 start_number:int = 0
 start_number_range:int = 5
 ts_from_file:IMAGE2_DEMUXER_TS_FROM_FILE = 'none'
 export_path_metadata:bool = False
 framerate:VIDEO_RATES = "25"
 pixel_format:str = None
 video_size:IMAGE_SIZES = None
 loop:bool = False 
 ...




@dataclass
class imagepipe_demuxer(): # imagepipe demuxer
 frame_size:int = 0
 framerate:VIDEO_RATES = "25"
 pixel_format:str = None
 video_size:IMAGE_SIZES = None
 loop:bool = False 
 ...


ALIAS_PIX_DEMUXER_PATTERN_TYPE = Literal['glob_sequence', 'glob', 'sequence', 'none']
ALIAS_PIX_DEMUXER_TS_FROM_FILE = Literal['none', 'sec', 'ns']

@dataclass
class alias_pix_demuxer(): # alias_pix demuxer
 pattern_type:ALIAS_PIX_DEMUXER_PATTERN_TYPE = '4'
 start_number:int = 0
 start_number_range:int = 5
 ts_from_file:ALIAS_PIX_DEMUXER_TS_FROM_FILE = 'none'
 export_path_metadata:bool = False
 framerate:VIDEO_RATES = "25"
 pixel_format:str = None
 video_size:IMAGE_SIZES = None
 loop:bool = False 
 ...


BRENDER_PIX_DEMUXER_PATTERN_TYPE = Literal['glob_sequence', 'glob', 'sequence', 'none']
BRENDER_PIX_DEMUXER_TS_FROM_FILE = Literal['none', 'sec', 'ns']

@dataclass
class brender_pix_demuxer(): # brender_pix demuxer
 pattern_type:BRENDER_PIX_DEMUXER_PATTERN_TYPE = '4'
 start_number:int = 0
 start_number_range:int = 5
 ts_from_file:BRENDER_PIX_DEMUXER_TS_FROM_FILE = 'none'
 export_path_metadata:bool = False
 framerate:VIDEO_RATES = "25"
 pixel_format:str = None
 video_size:IMAGE_SIZES = None
 loop:bool = False 
 ...




@dataclass
class imf(): # imf
 assetmaps:str = None 
 ...




@dataclass
class microdvddec(): # microdvddec
 subfps:float|str = '0/1' 
 ...


MOV_MP4_M4A_3GP_3G2_MJ2_USE_MFRA_FOR = Literal['auto', 'dts', 'pts']

@dataclass
class mov_mp4_m4a_3gp_3g2_mj2(): # mov,mp4,m4a,3gp,3g2,mj2
 use_absolute_path:bool = False
 seek_streams_individually:bool = True
 ignore_editlist:bool = False
 advanced_editlist:bool = True
 ignore_chapters:bool = False
 use_mfra_for:MOV_MP4_M4A_3GP_3G2_MJ2_USE_MFRA_FOR = 'auto'
 use_tfdt:bool = True
 export_all:bool = False
 export_xmp:bool = False
 activation_bytes:str = None
 audible_key:str = None
 audible_iv:str = None
 audible_fixed_key:str = None
 decryption_key:str = None
 enable_drefs:bool = False
 max_stts_delta:int = 4294487295 
 ...




@dataclass
class mp3(): # mp3
 usetoc:bool = False 
 ...




@dataclass
class mpegts_demuxer(): # mpegts demuxer
 resync_size:int = 65536
 fix_teletext_pts:bool = True
 ts_packetsize:int = 0
 scan_all_pmts:bool = 'auto'
 skip_unknown_pmt:bool = False
 merge_pmt_versions:bool = False
 max_packet_size:int = 204800 
 ...




@dataclass
class mpegtsraw_demuxer(): # mpegtsraw demuxer
 resync_size:int = 65536
 compute_pcr:bool = False
 ts_packetsize:int = 0 
 ...




@dataclass
class MPJPEG_demuxer(): # MPJPEG demuxer
 strict_mime_boundary:bool = False 
 ...




@dataclass
class mxf(): # mxf
 eia608_extract:bool = False 
 ...




@dataclass
class pcm_demuxer(): # pcm demuxer
 sample_rate:int = 44100
 channels:int = 1
 ch_layout:CHANNEL_LAYOUTS = None 
 ...




@dataclass
class rawvideo_demuxer(): # rawvideo demuxer
 pixel_format:str = "yuv420p"
 video_size:IMAGE_SIZES = None
 framerate:VIDEO_RATES = "25" 
 ...


RTP_DEMUXER_RTP_FLAGS = Literal['filter_src']
RTP_DEMUXER_ALLOWED_MEDIA_TYPES = Literal['video', 'audio', 'data', 'subtitle']

@dataclass
class RTP_demuxer(): # RTP demuxer
 rtp_flags:RTP_DEMUXER_RTP_FLAGS = '0'
 listen_timeout:str = '10'
 localaddr:str = None
 allowed_media_types:RTP_DEMUXER_ALLOWED_MEDIA_TYPES = 'video+audio+data+subtitle'
 reorder_queue_size:int = -1
 buffer_size:int = -1
 pkt_size:int = 1472 
 ...


RTSP_DEMUXER_RTPFLAGS = Literal['latm', 'rfc2190', 'skip_rtcp', 'h264_mode0', 'send_bye']
RTSP_DEMUXER_RTSP_TRANSPORT = Literal['udp', 'tcp', 'udp_multicast', 'http', 'https']
RTSP_DEMUXER_RTSP_FLAGS = Literal['filter_src', 'listen', 'prefer_tcp', 'satip_raw']
RTSP_DEMUXER_ALLOWED_MEDIA_TYPES = Literal['video', 'audio', 'data', 'subtitle']

@dataclass
class RTSP_demuxer(): # RTSP demuxer
 initial_pause:bool = False
 rtpflags:RTSP_DEMUXER_RTPFLAGS = '0'
 rtsp_transport:RTSP_DEMUXER_RTSP_TRANSPORT = '0'
 rtsp_flags:RTSP_DEMUXER_RTSP_FLAGS = '0'
 allowed_media_types:RTSP_DEMUXER_ALLOWED_MEDIA_TYPES = 'video+audio+data+subtitle'
 min_port:int = 5000
 max_port:int = 65000
 listen_timeout:int = -1
 timeout:int = 0
 reorder_queue_size:int = -1
 buffer_size:int = -1
 pkt_size:int = 1472
 user_agent:str = "Lavf60.3.100" 
 ...




@dataclass
class sbg_demuxer(): # sbg_demuxer
 sample_rate:int = 0
 frame_size:int = 0
 max_file_size:int = 5000000 
 ...


SDP_DEMUXER_SDP_FLAGS = Literal['filter_src', 'custom_io', 'rtcp_to_source']
SDP_DEMUXER_ALLOWED_MEDIA_TYPES = Literal['video', 'audio', 'data', 'subtitle']

@dataclass
class SDP_demuxer(): # SDP demuxer
 sdp_flags:SDP_DEMUXER_SDP_FLAGS = '0'
 listen_timeout:str = '10'
 localaddr:str = None
 allowed_media_types:SDP_DEMUXER_ALLOWED_MEDIA_TYPES = 'video+audio+data+subtitle'
 reorder_queue_size:int = -1
 buffer_size:int = -1
 pkt_size:int = 1472 
 ...




@dataclass
class ser_demuxer(): # ser demuxer
 framerate:VIDEO_RATES = "25" 
 ...




@dataclass
class sln_demuxer(): # sln demuxer
 sample_rate:int = 8000
 channels:int = 1
 ch_layout:CHANNEL_LAYOUTS = None 
 ...




@dataclass
class tedcaptions_demuxer(): # tedcaptions_demuxer
 start_time:int = 15000 
 ...




@dataclass
class TTY_demuxer(): # TTY demuxer
 chars_per_frame:int = 6000
 video_size:IMAGE_SIZES = None
 framerate:VIDEO_RATES = "25" 
 ...




@dataclass
class v210_x__demuxer(): # v210(x) demuxer
 video_size:IMAGE_SIZES = None
 framerate:VIDEO_RATES = "25" 
 ...




@dataclass
class vobsub(): # vobsub
 sub_name:str = None 
 ...




@dataclass
class W64_demuxer(): # W64 demuxer
 max_size:int = 4096 
 ...




@dataclass
class WAV_demuxer(): # WAV demuxer
 ignore_length:bool = False
 max_size:int = 4096 
 ...




@dataclass
class WebM_DASH_Manifest_demuxer(): # WebM DASH Manifest demuxer
 live:bool = False
 bandwidth:int = 0 
 ...


WEBVTT_DEMUXER_KIND = Literal['subtitles', 'captions', 'descriptions', 'metadata']

@dataclass
class WebVTT_demuxer(): # WebVTT demuxer
 kind:WEBVTT_DEMUXER_KIND = 'subtitles' 
 ...




@dataclass
class eXtended_BINary_text__XBIN__demuxer(): # eXtended BINary text (XBIN) demuxer
 linespeed:int = 6000
 video_size:IMAGE_SIZES = None
 framerate:VIDEO_RATES = "25" 
 ...




@dataclass
class AVFoundation_indev(): # AVFoundation indev
 list_devices:bool = False
 video_device_index:int = -1
 audio_device_index:int = -1
 pixel_format:PIXEL_FORMATS = 'yuv420p'
 framerate:VIDEO_RATES = "ntsc"
 video_size:IMAGE_SIZES = None
 capture_cursor:bool = False
 capture_mouse_clicks:bool = False
 capture_raw_data:bool = False
 drop_late_frames:bool = True 
 ...




@dataclass
class lavfi_indev(): # lavfi indev
 graph:str = None
 graph_file:str = None
 dumpgraph:str = None 
 ...


XCBGRAB_INDEV_FOLLOW_MOUSE = Literal['centered']

@dataclass
class xcbgrab_indev(): # xcbgrab indev
 window_id:int = 0
 x:int = 0
 y:int = 0
 grab_x:int = 0
 grab_y:int = 0
 video_size:IMAGE_SIZES = None
 framerate:str = "ntsc"
 draw_mouse:int = 1
 follow_mouse:XCBGRAB_INDEV_FOLLOW_MOUSE = '0'
 show_region:int = 0
 region_border:int = 3
 select_region:bool = False 
 ...


SWSCALER_SWS_FLAGS = Literal['fast_bilinear', 'bilinear', 'bicubic', 'experimental', 'neighbor', 'area', 'bicublin', 'gauss', 'sinc', 'lanczos', 'spline', 'print_info', 'accurate_rnd', 'full_chroma_int', 'full_chroma_inp', 'bitexact', 'error_diffusion']
SWSCALER_SWS_DITHER = Literal['auto', 'bayer', 'ed', 'a_dither', 'x_dither']
SWSCALER_ALPHABLEND = Literal['none', 'uniform_color', 'checkerboard']
SWSCALER_THREADS = Literal['auto']

@dataclass
class SWScaler(): # SWScaler
 sws_flags:SWSCALER_SWS_FLAGS = 'bicubic'
 srcw:int = 16
 srch:int = 16
 dstw:int = 16
 dsth:int = 16
 src_format:PIXEL_FORMATS = 'yuv420p'
 dst_format:PIXEL_FORMATS = 'yuv420p'
 src_range:bool = False
 dst_range:bool = False
 param0:float = '123456'
 param1:float = '123456'
 src_v_chr_pos:int = -513
 src_h_chr_pos:int = -513
 dst_v_chr_pos:int = -513
 dst_h_chr_pos:int = -513
 sws_dither:SWSCALER_SWS_DITHER = 'auto'
 gamma:bool = False
 alphablend:SWSCALER_ALPHABLEND = 'none'
 threads:SWSCALER_THREADS = '1' 
 ...


SWRESAMPLER_FLAGS = Literal['res']
SWRESAMPLER_DITHER_METHOD = Literal['rectangular', 'triangular', 'triangular_hp', 'lipshitz', 'shibata', 'low_shibata', 'high_shibata', 'f_weighted', 'modified_e_weighted', 'improved_e_weighted']
SWRESAMPLER_RESAMPLER = Literal['swr', 'soxr']
SWRESAMPLER_MATRIX_ENCODING = Literal['none', 'dolby', 'dplii']
SWRESAMPLER_FILTER_TYPE = Literal['cubic', 'blackman_nuttall', 'kaiser']

@dataclass
class SWResampler(): # SWResampler
 ich:int = 0
 in_channel_count:int = 0
 och:int = 0
 out_channel_count:int = 0
 uch:int = 0
 used_channel_count:int = 0
 isr:int = 0
 in_sample_rate:int = 0
 osr:int = 0
 out_sample_rate:int = 0
 isf:SAMPLE_RMT = 'none'
 in_sample_fmt:SAMPLE_RMT = 'none'
 osf:SAMPLE_RMT = 'none'
 out_sample_fmt:SAMPLE_RMT = 'none'
 tsf:SAMPLE_RMT = 'none'
 internal_sample_fmt:SAMPLE_RMT = 'none'
 icl:CHANNEL_LAYOUTS = '0x0'
 in_channel_layout:CHANNEL_LAYOUTS = '0x0'
 ocl:CHANNEL_LAYOUTS = '0x0'
 out_channel_layout:CHANNEL_LAYOUTS = '0x0'
 ichl:CHANNEL_LAYOUTS = None
 in_chlayout:CHANNEL_LAYOUTS = None
 ochl:CHANNEL_LAYOUTS = None
 out_chlayout:CHANNEL_LAYOUTS = None
 uchl:CHANNEL_LAYOUTS = None
 used_chlayout:CHANNEL_LAYOUTS = None
 clev:float = '0.707107'
 center_mix_level:float = '0.707107'
 slev:float = '0.707107'
 surround_mix_level:float = '0.707107'
 lfe_mix_level:float = '0'
 rmvol:float = '1'
 rematrix_volume:float = '1'
 rematrix_maxval:float = '0'
 flags:SWRESAMPLER_FLAGS = '0'
 swr_flags:SWRESAMPLER_FLAGS = '0'
 dither_scale:float = '1'
 dither_method:SWRESAMPLER_DITHER_METHOD = '0'
 filter_size:int = 32
 phase_shift:int = 10
 linear_interp:bool = True
 exact_rational:bool = True
 cutoff:float = '0'
 resample_cutoff:float = '0'
 resampler:SWRESAMPLER_RESAMPLER = 'swr'
 precision:float = '20'
 cheby:bool = False
 min_comp:float = 'FLT_MAX'
 min_hard_comp:float = '0.1'
 comp_duration:float = '1'
 max_soft_comp:float = '0'
 _async:float = dataclasses_field(default='0', metadata='async')
 first_pts:int = 'I64_MIN'
 matrix_encoding:SWRESAMPLER_MATRIX_ENCODING = 'none'
 filter_type:SWRESAMPLER_FILTER_TYPE = 'kaiser'
 kaiser_beta:float = '9'
 output_sample_bits:int = 0 
 ...


AVFILTER_THREAD_TYPE = Literal['slice']

@dataclass
class AVFilter(): # AVFilter
 thread_type:AVFILTER_THREAD_TYPE = 'slice'
 enable:str = None
 threads:int = 0
 extra_hw_frames:int = -1 
 ...


ABENCH_ACTION = Literal['start', 'stop']

@dataclass
class abench(): # abench
 action:ABENCH_ACTION = 'start' 
 ...


ACOMPRESSOR_SIDECHAINCOMPRESS_MODE = Literal['downward', 'upward']
ACOMPRESSOR_SIDECHAINCOMPRESS_LINK = Literal['average', 'maximum']
ACOMPRESSOR_SIDECHAINCOMPRESS_DETECTION = Literal['peak', 'rms']

@dataclass
class acompressor_sidechaincompress(): # acompressor/sidechaincompress
 level_in:float = '1'
 mode:ACOMPRESSOR_SIDECHAINCOMPRESS_MODE = 'downward'
 threshold:float = '0.125'
 ratio:float = '2'
 attack:float = '20'
 release:float = '250'
 makeup:float = '1'
 knee:float = '2.82843'
 link:ACOMPRESSOR_SIDECHAINCOMPRESS_LINK = 'average'
 detection:ACOMPRESSOR_SIDECHAINCOMPRESS_DETECTION = 'rms'
 level_sc:float = '1'
 mix:float = '1' 
 ...




@dataclass
class acontrast(): # acontrast
 contrast:float = '33' 
 ...




@dataclass
class _a_cue(): # (a)cue
 cue:int = 0
 preroll:str = '0'
 buffer:str = '0' 
 ...


ACROSSFADE_CURVE1 = Literal['nofade', 'tri', 'qsin', 'esin', 'hsin', 'log', 'ipar', 'qua', 'cub', 'squ', 'cbr', 'par', 'exp', 'iqsin', 'ihsin', 'dese', 'desi', 'losi', 'sinc', 'isinc']

@dataclass
class acrossfade(): # acrossfade
 nb_samples:int = 44100
 ns:int = 44100
 duration:str = '0'
 d:str = '0'
 overlap:bool = True
 o:bool = True
 curve1:ACROSSFADE_CURVE1 = 'tri'
 c1:ACROSSFADE_CURVE1 = 'tri'
 curve2:ACROSSFADE_CURVE1 = 'tri'
 c2:ACROSSFADE_CURVE1 = 'tri' 
 ...


ACROSSOVER_ORDER = Literal['2nd', '4th', '6th', '8th', '10th', '12th', '14th', '16th', '18th', '20th']
ACROSSOVER_PRECISION = Literal['auto', 'float', 'double']

@dataclass
class acrossover(): # acrossover
 split:str = "500"
 order:ACROSSOVER_ORDER = '4th'
 level:float = '1'
 gain:str = "1.f"
 precision:ACROSSOVER_PRECISION = 'auto' 
 ...


ACRUSHER_MODE = Literal['lin', 'log']

@dataclass
class acrusher(): # acrusher
 level_in:float = '1'
 level_out:float = '1'
 bits:float = '8'
 mix:float = '0.5'
 mode:ACRUSHER_MODE = 'lin'
 dc:float = '1'
 aa:float = '0.5'
 samples:float = '1'
 lfo:bool = False
 lforange:float = '20'
 lforate:float = '0.3' 
 ...


ADECLICK_METHOD = Literal['add', 'a', 'save', 's']

@dataclass
class adeclick(): # adeclick
 window:float = '55'
 w:float = '55'
 overlap:float = '75'
 o:float = '75'
 arorder:float = '2'
 a:float = '2'
 threshold:float = '2'
 t:float = '2'
 burst:float = '2'
 b:float = '2'
 method:ADECLICK_METHOD = 'add'
 m:ADECLICK_METHOD = 'add' 
 ...


ADECLIP_METHOD = Literal['add', 'a', 'save', 's']

@dataclass
class adeclip(): # adeclip
 window:float = '55'
 w:float = '55'
 overlap:float = '75'
 o:float = '75'
 arorder:float = '8'
 a:float = '8'
 threshold:float = '10'
 t:float = '10'
 hsize:int = 1000
 n:int = 1000
 method:ADECLIP_METHOD = 'add'
 m:ADECLIP_METHOD = 'add' 
 ...




@dataclass
class adecorrelate(): # adecorrelate
 stages:int = 6
 seed:int = -1 
 ...




@dataclass
class adelay(): # adelay
 delays:str = None
 all:bool = False 
 ...


ADENORM_TYPE = Literal['dc', 'ac', 'square', 'pulse']

@dataclass
class adenorm(): # adenorm
 level:float = '-351'
 type:ADENORM_TYPE = 'dc' 
 ...




@dataclass
class aderivative_aintegral(): # aderivative/aintegral 
 ...




@dataclass
class adrc(): # adrc
 transfer:str = "p"
 attack:float = '50'
 release:float = '100'
 channels:str = "all" 
 ...


ADYNAMICEQUALIZER_MODE = Literal['listen', 'cut', 'boost']
ADYNAMICEQUALIZER_TFTYPE = Literal['bell', 'lowshelf', 'highshelf']
ADYNAMICEQUALIZER_DIRECTION = Literal['downward', 'upward']
ADYNAMICEQUALIZER_AUTO = Literal['disabled', 'off', 'on']

@dataclass
class adynamicequalizer(): # adynamicequalizer
 threshold:float = '0'
 dfrequency:float = '1000'
 dqfactor:float = '1'
 tfrequency:float = '1000'
 tqfactor:float = '1'
 attack:float = '20'
 release:float = '200'
 ratio:float = '1'
 makeup:float = '0'
 range:float = '50'
 mode:ADYNAMICEQUALIZER_MODE = 'cut'
 tftype:ADYNAMICEQUALIZER_TFTYPE = 'bell'
 direction:ADYNAMICEQUALIZER_DIRECTION = 'downward'
 auto:ADYNAMICEQUALIZER_AUTO = 'disabled' 
 ...




@dataclass
class adynamicsmooth(): # adynamicsmooth
 sensitivity:float = '2'
 basefreq:float = '22050' 
 ...




@dataclass
class aecho(): # aecho
 in_gain:float = '0.6'
 out_gain:float = '0.3'
 delays:str = "1000"
 decays:str = "0.5" 
 ...


AEMPHASIS_MODE = Literal['reproduction', 'production']
AEMPHASIS_TYPE = Literal['col', 'emi', 'bsi', 'riaa', 'cd', '50fm', '75fm', '50kf', '75kf']

@dataclass
class aemphasis(): # aemphasis
 level_in:float = '1'
 level_out:float = '1'
 mode:AEMPHASIS_MODE = 'reproduction'
 type:AEMPHASIS_TYPE = 'cd' 
 ...




@dataclass
class aeval(): # aeval
 exprs:str = None
 channel_layout:str = None
 c:str = None 
 ...




@dataclass
class aexciter(): # aexciter
 level_in:float = '1'
 level_out:float = '1'
 amount:float = '1'
 drive:float = '8.5'
 blend:float = '0'
 freq:float = '7500'
 ceil:float = '9999'
 listen:bool = False 
 ...


AFADE_TYPE = Literal['in', 'out']
AFADE_CURVE = Literal['nofade', 'tri', 'qsin', 'esin', 'hsin', 'log', 'ipar', 'qua', 'cub', 'squ', 'cbr', 'par', 'exp', 'iqsin', 'ihsin', 'dese', 'desi', 'losi', 'sinc', 'isinc']

@dataclass
class afade(): # afade
 type:AFADE_TYPE = 'in'
 t:AFADE_TYPE = 'in'
 start_sample:int = 0
 ss:int = 0
 nb_samples:int = 44100
 ns:int = 44100
 start_time:str = '0'
 st:str = '0'
 duration:str = '0'
 d:str = '0'
 curve:AFADE_CURVE = 'tri'
 c:AFADE_CURVE = 'tri'
 silence:float = '0'
 unity:float = '1' 
 ...


AFFTDN_NOISE_TYPE = Literal['white', 'w', 'vinyl', 'v', 'shellac', 's', 'custom', 'c']
AFFTDN_OUTPUT_MODE = Literal['input', 'i', 'output', 'o', 'noise', 'n']
AFFTDN_NOISE_LINK = Literal['none', 'min', 'max', 'average']
AFFTDN_SAMPLE_NOISE = Literal['none', 'start', 'begin', 'stop', 'end']

@dataclass
class afftdn(): # afftdn
 noise_reduction:float = '12'
 nr:float = '12'
 noise_floor:float = '-50'
 nf:float = '-50'
 noise_type:AFFTDN_NOISE_TYPE = 'white'
 nt:AFFTDN_NOISE_TYPE = 'white'
 band_noise:str = None
 bn:str = None
 residual_floor:float = '-38'
 rf:float = '-38'
 track_noise:bool = False
 tn:bool = False
 track_residual:bool = False
 tr:bool = False
 output_mode:AFFTDN_OUTPUT_MODE = 'output'
 om:AFFTDN_OUTPUT_MODE = 'output'
 adaptivity:float = '0.5'
 ad:float = '0.5'
 floor_offset:float = '1'
 fo:float = '1'
 noise_link:AFFTDN_NOISE_LINK = 'min'
 nl:AFFTDN_NOISE_LINK = 'min'
 band_multiplier:float = '1.25'
 bm:float = '1.25'
 sample_noise:AFFTDN_SAMPLE_NOISE = 'none'
 sn:AFFTDN_SAMPLE_NOISE = 'none'
 gain_smooth:int = 0
 gs:int = 0 
 ...


AFFTFILT_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']

@dataclass
class afftfilt(): # afftfilt
 real:str = "re"
 imag:str = "im"
 win_size:int = 4096
 win_func:AFFTFILT_WIN_FUNC = 'hann'
 overlap:float = '0.75' 
 ...


AFIR_GTYPE = Literal['none', 'peak', 'dc', 'gn', 'ac', 'rms']
AFIR_IRFMT = Literal['mono', 'input']
AFIR_PRECISION = Literal['auto', 'float', 'double']

@dataclass
class afir(): # afir
 dry:float = '1'
 wet:float = '1'
 length:float = '1'
 gtype:AFIR_GTYPE = 'peak'
 irgain:float = '1'
 irfmt:AFIR_IRFMT = 'input'
 maxir:float = '30'
 response:bool = False
 channel:int = 0
 size:IMAGE_SIZES = "hd720"
 rate:VIDEO_RATES = "25"
 minp:int = 8192
 maxp:int = 8192
 nbirs:int = 1
 ir:int = 0
 precision:AFIR_PRECISION = 'auto' 
 ...




@dataclass
class aformat(): # aformat
 sample_fmts:str = None
 f:str = None
 sample_rates:str = None
 r:str = None
 channel_layouts:str = None
 cl:str = None 
 ...




@dataclass
class afreqshift(): # afreqshift
 shift:float = '0'
 level:float = '1'
 order:int = 8 
 ...


AFWTDN_WAVET = Literal['sym2', 'sym4', 'rbior68', 'deb10', 'sym10', 'coif5', 'bl3']

@dataclass
class afwtdn(): # afwtdn
 sigma:float = '0'
 levels:int = 10
 wavet:AFWTDN_WAVET = 'sym10'
 percent:float = '85'
 profile:bool = False
 adaptive:bool = False
 samples:int = 8192
 softness:float = '1' 
 ...


AGATE_SIDECHAINGATE_MODE = Literal['downward', 'upward']
AGATE_SIDECHAINGATE_DETECTION = Literal['peak', 'rms']
AGATE_SIDECHAINGATE_LINK = Literal['average', 'maximum']

@dataclass
class agate_sidechaingate(): # agate/sidechaingate
 level_in:float = '1'
 mode:AGATE_SIDECHAINGATE_MODE = 'downward'
 range:float = '0.06125'
 threshold:float = '0.125'
 ratio:float = '2'
 attack:float = '20'
 release:float = '250'
 makeup:float = '1'
 knee:float = '2.82843'
 detection:AGATE_SIDECHAINGATE_DETECTION = 'rms'
 link:AGATE_SIDECHAINGATE_LINK = 'average'
 level_sc:float = '1' 
 ...


AIIR_FORMAT = Literal['ll', 'sf', 'tf', 'zp', 'pr', 'pd', 'sp']
AIIR_PROCESS = Literal['d', 's', 'p']
AIIR_PRECISION = Literal['dbl', 'flt', 'i32', 'i16']

@dataclass
class aiir(): # aiir
 zeros:str = "1+0i 1-0i"
 z:str = "1+0i 1-0i"
 poles:str = "1+0i 1-0i"
 p:str = "1+0i 1-0i"
 gains:str = "1|1"
 k:str = "1|1"
 dry:float = '1'
 wet:float = '1'
 format:AIIR_FORMAT = 'zp'
 f:AIIR_FORMAT = 'zp'
 process:AIIR_PROCESS = 's'
 r:AIIR_PROCESS = 's'
 precision:AIIR_PRECISION = 'dbl'
 e:AIIR_PRECISION = 'dbl'
 normalize:bool = True
 n:bool = True
 mix:float = '1'
 response:bool = False
 channel:int = 0
 size:IMAGE_SIZES = "hd720"
 rate:VIDEO_RATES = "25" 
 ...


AINTERLEAVE_DURATION = Literal['longest', 'shortest', 'first']

@dataclass
class ainterleave(): # ainterleave
 nb_inputs:int = 2
 n:int = 2
 duration:AINTERLEAVE_DURATION = 'longest' 
 ...




@dataclass
class alimiter(): # alimiter
 level_in:float = '1'
 level_out:float = '1'
 limit:float = '1'
 attack:float = '5'
 release:float = '50'
 asc:bool = False
 asc_level:float = '0.5'
 level:bool = True
 latency:bool = False 
 ...


ALLPASS_WIDTH_TYPE = Literal['h', 'q', 'o', 's', 'k']
ALLPASS_TRANSFORM = Literal['di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf']
ALLPASS_PRECISION = Literal['auto', 's16', 's32', 'f32', 'f64']

@dataclass
class allpass(): # allpass
 frequency:float = '3000'
 f:float = '3000'
 width_type:ALLPASS_WIDTH_TYPE = 'q'
 t:ALLPASS_WIDTH_TYPE = 'q'
 width:float = '0.707'
 w:float = '0.707'
 mix:float = '1'
 m:float = '1'
 channels:str = "all"
 c:str = "all"
 normalize:bool = False
 n:bool = False
 order:int = 2
 o:int = 2
 transform:ALLPASS_TRANSFORM = 'di'
 a:ALLPASS_TRANSFORM = 'di'
 precision:ALLPASS_PRECISION = 'auto'
 r:ALLPASS_PRECISION = 'auto' 
 ...




@dataclass
class aloop(): # aloop
 loop:int = 0
 size:int = 0
 start:int = 0 
 ...




@dataclass
class amerge(): # amerge
 inputs:int = 2 
 ...


AMETADATA_MODE = Literal['select', 'add', 'modify', 'delete', 'print']
AMETADATA_FUNCTION = Literal['same_str', 'starts_with', 'less', 'equal', 'greater', 'expr', 'ends_with']

@dataclass
class ametadata(): # ametadata
 mode:AMETADATA_MODE = 'select'
 key:str = None
 value:str = None
 function:AMETADATA_FUNCTION = 'same_str'
 expr:str = None
 file:str = None
 direct:bool = False 
 ...


AMIX_DURATION = Literal['longest', 'shortest', 'first']

@dataclass
class amix(): # amix
 inputs:int = 2
 duration:AMIX_DURATION = 'longest'
 dropout_transition:float = '2'
 weights:str = "1 1"
 normalize:bool = True 
 ...


ANEQUALIZER_FSCALE = Literal['lin', 'log']

@dataclass
class anequalizer(): # anequalizer
 params:str = ""
 curves:bool = False
 size:IMAGE_SIZES = "hd720"
 mgain:float = '60'
 fscale:ANEQUALIZER_FSCALE = 'log'
 colors:str = "red|green|blue|yellow|orange|lime|pink|magenta|brown" 
 ...


ANLMDN_OUTPUT = Literal['i', 'o', 'n']

@dataclass
class anlmdn(): # anlmdn
 strength:float = '1e-05'
 s:float = '1e-05'
 patch:str = '0.002'
 p:str = '0.002'
 research:str = '0.006'
 r:str = '0.006'
 output:ANLMDN_OUTPUT = 'o'
 o:ANLMDN_OUTPUT = 'o'
 smooth:float = '11'
 m:float = '11' 
 ...


ANLM_F_S__OUT_MODE = Literal['i', 'd', 'o', 'n']

@dataclass
class anlm_f_s_(): # anlm(f|s)
 order:int = 256
 mu:float = '0.75'
 eps:float = '1'
 leakage:float = '0'
 out_mode:ANLM_F_S__OUT_MODE = 'o' 
 ...




@dataclass
class apad(): # apad
 packet_size:int = 4096
 pad_len:int = -1
 whole_len:int = -1
 pad_dur:str = '-0.000001'
 whole_dur:str = '-0.000001' 
 ...


_A_PERMS_MODE = Literal['none', 'ro', 'rw', 'toggle', 'random']

@dataclass
class _a_perms(): # (a)perms
 mode:_A_PERMS_MODE = 'none'
 seed:int = -1 
 ...


APHASER_TYPE = Literal['triangular', 't', 'sinusoidal', 's']

@dataclass
class aphaser(): # aphaser
 in_gain:float = '0.4'
 out_gain:float = '0.74'
 delay:float = '3'
 decay:float = '0.4'
 speed:float = '0.5'
 type:APHASER_TYPE = 'triangular' 
 ...




@dataclass
class aphaseshift(): # aphaseshift
 shift:float = '0'
 level:float = '1'
 order:int = 8 
 ...




@dataclass
class apsyclip(): # apsyclip
 level_in:float = '1'
 level_out:float = '1'
 clip:float = '1'
 diff:bool = False
 adaptive:float = '0.5'
 iterations:int = 10
 level:bool = False 
 ...


APULSATOR_MODE = Literal['sine', 'triangle', 'square', 'sawup', 'sawdown']
APULSATOR_TIMING = Literal['bpm', 'ms', 'hz']

@dataclass
class apulsator(): # apulsator
 level_in:float = '1'
 level_out:float = '1'
 mode:APULSATOR_MODE = 'sine'
 amount:float = '1'
 offset_l:float = '0'
 offset_r:float = '0.5'
 width:float = '1'
 timing:APULSATOR_TIMING = 'hz'
 bpm:float = '120'
 ms:int = 500
 hz:float = '2' 
 ...




@dataclass
class _a_realtime(): # (a)realtime
 limit:str = '2'
 speed:float = '1' 
 ...




@dataclass
class aresample(): # aresample
 sample_rate:int = 0 
 ...




@dataclass
class arnndn(): # arnndn
 model:str = None
 m:str = None
 mix:float = '1' 
 ...




@dataclass
class asegment(): # asegment
 timestamps:str = None
 samples:str = None 
 ...




@dataclass
class aselect(): # aselect
 expr:str = "1"
 e:str = "1"
 outputs:int = 1
 n:int = 1 
 ...




@dataclass
class _a_sendcmd(): # (a)sendcmd
 commands:str = None
 c:str = None
 filename:str = None
 f:str = None 
 ...




@dataclass
class asetnsamples(): # asetnsamples
 nb_out_samples:int = 1024
 n:int = 1024
 pad:bool = True
 p:bool = True 
 ...




@dataclass
class asetpts(): # asetpts
 expr:str = "PTS" 
 ...




@dataclass
class asetrate(): # asetrate
 sample_rate:int = 44100
 r:int = 44100 
 ...




@dataclass
class asettb(): # asettb
 expr:str = "intb"
 tb:str = "intb" 
 ...


ASIDEDATA_MODE = Literal['select', 'delete']
ASIDEDATA_TYPE = Literal['PANSCAN', 'A53_CC', 'STEREO3D', 'MATRIXENCODING', 'DOWNMIX_INFO', 'REPLAYGAIN', 'DISPLAYMATRIX', 'AFD', 'MOTION_VECTORS', 'SKIP_SAMPLES', 'AUDIO_SERVICE_TYPE', 'MASTERING_DISPLAY_METADATA', 'GOP_TIMECODE', 'SPHERICAL', 'CONTENT_LIGHT_LEVEL', 'ICC_PROFILE', 'S12M_TIMECOD', 'DYNAMIC_HDR_PLUS', 'REGIONS_OF_INTEREST', 'DETECTION_BOUNDING_BOXES', 'SEI_UNREGISTERED']

@dataclass
class asidedata(): # asidedata
 mode:ASIDEDATA_MODE = 'select'
 type:ASIDEDATA_TYPE = '-1' 
 ...


ASOFTCLIP_TYPE = Literal['hard', 'tanh', 'atan', 'cubic', 'exp', 'alg', 'quintic', 'sin', 'erf']

@dataclass
class asoftclip(): # asoftclip
 type:ASOFTCLIP_TYPE = 'tanh'
 threshold:float = '1'
 output:float = '1'
 param:float = '1'
 oversample:int = 1 
 ...


ASPECTRALSTATS_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']
ASPECTRALSTATS_MEASURE = Literal['none', 'all', 'mean', 'variance', 'centroid', 'spread', 'skewness', 'kurtosis', 'entropy', 'flatness', 'crest', 'flux', 'slope', 'decrease', 'rolloff']

@dataclass
class aspectralstats(): # aspectralstats
 win_size:int = 2048
 win_func:ASPECTRALSTATS_WIN_FUNC = 'hann'
 overlap:float = '0.5'
 measure:ASPECTRALSTATS_MEASURE = 'all+mean+variance+centroid+spread+skewness+kurtosis+entropy+flatness+crest+flux+slope+decrease+rolloff' 
 ...




@dataclass
class _a_split(): # (a)split
 outputs:int = 2 
 ...


ASTATS_MEASURE_PERCHANNEL = Literal['none', 'all', 'Bit_depth', 'Crest_factor', 'DC_offset', 'Dynamic_range', 'Entropy', 'Flat_factor', 'Max_difference', 'Max_level', 'Mean_difference', 'Min_difference', 'Min_level', 'Noise_floor', 'Noise_floor_count', 'Number_of_Infs', 'Number_of_NaNs', 'Number_of_denormals', 'Number_of_samples', 'Peak_count', 'Peak_level', 'RMS_difference', 'RMS_level', 'RMS_peak', 'RMS_trough', 'Zero_crossings', 'Zero_crossings_rate']

@dataclass
class astats(): # astats
 length:float = '0.05'
 metadata:bool = False
 reset:int = 0
 measure_perchannel:ASTATS_MEASURE_PERCHANNEL = 'all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate'
 measure_overall:ASTATS_MEASURE_PERCHANNEL = 'all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate' 
 ...




@dataclass
class _a_streamselect(): # (a)streamselect
 inputs:int = 2
 map:str = None 
 ...




@dataclass
class asubboost(): # asubboost
 dry:float = '1'
 wet:float = '1'
 boost:float = '2'
 decay:float = '0'
 feedback:float = '0.9'
 cutoff:float = '100'
 slope:float = '0.5'
 delay:float = '20'
 channels:str = "all" 
 ...




@dataclass
class asubcut(): # asubcut
 cutoff:float = '20'
 order:int = 10
 level:float = '1' 
 ...




@dataclass
class asupercut(): # asupercut
 cutoff:float = '20000'
 order:int = 10
 level:float = '1' 
 ...




@dataclass
class asuperpass_asuperstop(): # asuperpass/asuperstop
 centerf:float = '1000'
 order:int = 4
 qfactor:float = '1'
 level:float = '1' 
 ...




@dataclass
class atempo(): # atempo
 tempo:float = '1' 
 ...




@dataclass
class atilt(): # atilt
 freq:float = '10000'
 slope:float = '0'
 width:float = '1000'
 order:int = 5
 level:float = '1' 
 ...




@dataclass
class atrim(): # atrim
 start:str = 'INT64_MAX'
 starti:str = 'INT64_MAX'
 end:str = 'INT64_MAX'
 endi:str = 'INT64_MAX'
 start_pts:int = 'I64_MIN'
 end_pts:int = 'I64_MIN'
 duration:str = '0'
 durationi:str = '0'
 start_sample:int = -1
 end_sample:int = 'I64_MAX' 
 ...


AXCORRELATE_ALGO = Literal['slow', 'fast']

@dataclass
class axcorrelate(): # axcorrelate
 size:int = 256
 algo:AXCORRELATE_ALGO = 'slow' 
 ...




@dataclass
class _a_zmq(): # (a)zmq
 bind_address:str = "tcp://*:5555"
 b:str = "tcp://*:5555" 
 ...


BANDPASS_WIDTH_TYPE = Literal['h', 'q', 'o', 's', 'k']
BANDPASS_TRANSFORM = Literal['di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf']
BANDPASS_PRECISION = Literal['auto', 's16', 's32', 'f32', 'f64']

@dataclass
class bandpass(): # bandpass
 frequency:float = '3000'
 f:float = '3000'
 width_type:BANDPASS_WIDTH_TYPE = 'q'
 t:BANDPASS_WIDTH_TYPE = 'q'
 width:float = '0.5'
 w:float = '0.5'
 csg:bool = False
 mix:float = '1'
 m:float = '1'
 channels:str = "all"
 c:str = "all"
 normalize:bool = False
 n:bool = False
 transform:BANDPASS_TRANSFORM = 'di'
 a:BANDPASS_TRANSFORM = 'di'
 precision:BANDPASS_PRECISION = 'auto'
 r:BANDPASS_PRECISION = 'auto'
 blocksize:int = 0
 b:int = 0 
 ...


BANDREJECT_WIDTH_TYPE = Literal['h', 'q', 'o', 's', 'k']
BANDREJECT_TRANSFORM = Literal['di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf']
BANDREJECT_PRECISION = Literal['auto', 's16', 's32', 'f32', 'f64']

@dataclass
class bandreject(): # bandreject
 frequency:float = '3000'
 f:float = '3000'
 width_type:BANDREJECT_WIDTH_TYPE = 'q'
 t:BANDREJECT_WIDTH_TYPE = 'q'
 width:float = '0.5'
 w:float = '0.5'
 mix:float = '1'
 m:float = '1'
 channels:str = "all"
 c:str = "all"
 normalize:bool = False
 n:bool = False
 transform:BANDREJECT_TRANSFORM = 'di'
 a:BANDREJECT_TRANSFORM = 'di'
 precision:BANDREJECT_PRECISION = 'auto'
 r:BANDREJECT_PRECISION = 'auto'
 blocksize:int = 0
 b:int = 0 
 ...


BASS_LOWSHELF_WIDTH_TYPE = Literal['h', 'q', 'o', 's', 'k']
BASS_LOWSHELF_TRANSFORM = Literal['di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf']
BASS_LOWSHELF_PRECISION = Literal['auto', 's16', 's32', 'f32', 'f64']

@dataclass
class bass_lowshelf(): # bass/lowshelf
 frequency:float = '100'
 f:float = '100'
 width_type:BASS_LOWSHELF_WIDTH_TYPE = 'q'
 t:BASS_LOWSHELF_WIDTH_TYPE = 'q'
 width:float = '0.5'
 w:float = '0.5'
 gain:float = '0'
 g:float = '0'
 poles:int = 2
 p:int = 2
 mix:float = '1'
 m:float = '1'
 channels:str = "all"
 c:str = "all"
 normalize:bool = False
 n:bool = False
 transform:BASS_LOWSHELF_TRANSFORM = 'di'
 a:BASS_LOWSHELF_TRANSFORM = 'di'
 precision:BASS_LOWSHELF_PRECISION = 'auto'
 r:BASS_LOWSHELF_PRECISION = 'auto'
 blocksize:int = 0
 b:int = 0 
 ...


BIQUAD_TRANSFORM = Literal['di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf']
BIQUAD_PRECISION = Literal['auto', 's16', 's32', 'f32', 'f64']

@dataclass
class biquad(): # biquad
 a0:float = '1'
 a1:float = '0'
 a2:float = '0'
 b0:float = '0'
 b1:float = '0'
 b2:float = '0'
 mix:float = '1'
 m:float = '1'
 channels:str = "all"
 c:str = "all"
 normalize:bool = False
 n:bool = False
 transform:BIQUAD_TRANSFORM = 'di'
 a:BIQUAD_TRANSFORM = 'di'
 precision:BIQUAD_PRECISION = 'auto'
 r:BIQUAD_PRECISION = 'auto'
 blocksize:int = 0
 b:int = 0 
 ...




@dataclass
class channelmap(): # channelmap
 map:str = None
 channel_layout:str = None 
 ...




@dataclass
class channelsplit(): # channelsplit
 channel_layout:str = "stereo"
 channels:str = "all" 
 ...




@dataclass
class chorus(): # chorus
 in_gain:float = '0.4'
 out_gain:float = '0.4'
 delays:str = None
 decays:str = None
 speeds:str = None
 depths:str = None 
 ...




@dataclass
class compand(): # compand
 attacks:str = "0"
 decays:str = "0.8"
 points:str = "-70/-70|-60/-20|1/0"
 soft_knee:float = dataclasses_field(default='0.01', metadata='soft-knee')
 gain:float = '0'
 volume:float = '0'
 delay:float = '0' 
 ...




@dataclass
class compensationdelay(): # compensationdelay
 mm:int = 0
 cm:int = 0
 m:int = 0
 dry:float = '0'
 wet:float = '1'
 temp:int = 20 
 ...




@dataclass
class crossfeed(): # crossfeed
 strength:float = '0.2'
 range:float = '0.5'
 slope:float = '0.5'
 level_in:float = '0.9'
 level_out:float = '1'
 block_size:int = 0 
 ...




@dataclass
class crystalizer(): # crystalizer
 i:float = '2'
 c:bool = True 
 ...




@dataclass
class dcshift(): # dcshift
 shift:float = '0'
 limitergain:float = '0' 
 ...


DEESSER_S = Literal['i', 'o', 'e']

@dataclass
class deesser(): # deesser
 i:float = '0'
 m:float = '0.5'
 f:float = '0.5'
 s:DEESSER_S = 'o' 
 ...




@dataclass
class dialoguenhance(): # dialoguenhance
 original:float = '1'
 enhance:float = '1'
 voice:float = '2' 
 ...




@dataclass
class drmeter(): # drmeter
 length:float = '3' 
 ...




@dataclass
class dynaudnorm(): # dynaudnorm
 framelen:int = 500
 f:int = 500
 gausssize:int = 31
 g:int = 31
 peak:float = '0.95'
 p:float = '0.95'
 maxgain:float = '10'
 m:float = '10'
 targetrms:float = '0'
 r:float = '0'
 coupling:bool = True
 n:bool = True
 correctdc:bool = False
 c:bool = False
 altboundary:bool = False
 b:bool = False
 compress:float = '0'
 s:float = '0'
 threshold:float = '0'
 t:float = '0'
 channels:str = "all"
 h:str = "all"
 overlap:float = '0'
 o:float = '0'
 curve:str = None
 v:str = None 
 ...


EBUR128_FRAMELOG = Literal['quiet', 'info', 'verbose']
EBUR128_PEAK = Literal['none', 'sample', 'true']
EBUR128_GAUGE = Literal['momentary', 'm', 'shortterm', 's']
EBUR128_SCALE = Literal['absolute', 'LUFS', 'relative', 'LU']

@dataclass
class ebur128(): # ebur128
 video:bool = False
 size:IMAGE_SIZES = "640x480"
 meter:int = 9
 framelog:EBUR128_FRAMELOG = '-1'
 metadata:bool = False
 peak:EBUR128_PEAK = '0'
 dualmono:bool = False
 panlaw:float = '-3.0103'
 target:int = -23
 gauge:EBUR128_GAUGE = 'momentary'
 scale:EBUR128_SCALE = 'absolute' 
 ...


EQUALIZER_WIDTH_TYPE = Literal['h', 'q', 'o', 's', 'k']
EQUALIZER_TRANSFORM = Literal['di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf']
EQUALIZER_PRECISION = Literal['auto', 's16', 's32', 'f32', 'f64']

@dataclass
class equalizer(): # equalizer
 frequency:float = '0'
 f:float = '0'
 width_type:EQUALIZER_WIDTH_TYPE = 'q'
 t:EQUALIZER_WIDTH_TYPE = 'q'
 width:float = '1'
 w:float = '1'
 gain:float = '0'
 g:float = '0'
 mix:float = '1'
 m:float = '1'
 channels:str = "all"
 c:str = "all"
 normalize:bool = False
 n:bool = False
 transform:EQUALIZER_TRANSFORM = 'di'
 a:EQUALIZER_TRANSFORM = 'di'
 precision:EQUALIZER_PRECISION = 'auto'
 r:EQUALIZER_PRECISION = 'auto'
 blocksize:int = 0
 b:int = 0 
 ...




@dataclass
class extrastereo(): # extrastereo
 m:float = '2.5'
 c:bool = True 
 ...


FIREQUALIZER_WFUNC = Literal['rectangular', 'hann', 'hamming', 'blackman', 'nuttall3', 'mnuttall3', 'nuttall', 'bnuttall', 'bharris', 'tukey']
FIREQUALIZER_SCALE = Literal['linlin', 'linlog', 'loglin', 'loglog']

@dataclass
class firequalizer(): # firequalizer
 gain:str = None
 gain_entry:str = None
 delay:float = '0.01'
 accuracy:float = '5'
 wfunc:FIREQUALIZER_WFUNC = 'hann'
 fixed:bool = False
 multi:bool = False
 zero_phase:bool = False
 scale:FIREQUALIZER_SCALE = 'linlog'
 dumpfile:str = None
 dumpscale:FIREQUALIZER_SCALE = 'linlog'
 fft2:bool = False
 min_phase:bool = False 
 ...


FLANGER_SHAPE = Literal['triangular', 't', 'sinusoidal', 's']
FLANGER_INTERP = Literal['linear', 'quadratic']

@dataclass
class flanger(): # flanger
 delay:float = '0'
 depth:float = '2'
 regen:float = '0'
 width:float = '71'
 speed:float = '0.5'
 shape:FLANGER_SHAPE = 'sinusoidal'
 phase:float = '25'
 interp:FLANGER_INTERP = 'linear' 
 ...


HAAS_MIDDLE_SOURCE = Literal['left', 'right', 'mid', 'side']

@dataclass
class haas(): # haas
 level_in:float = '1'
 level_out:float = '1'
 side_gain:float = '1'
 middle_source:HAAS_MIDDLE_SOURCE = 'mid'
 middle_phase:bool = False
 left_delay:float = '2.05'
 left_balance:float = '-1'
 left_gain:float = '1'
 left_phase:bool = False
 right_delay:float = '2.12'
 right_balance:float = '1'
 right_gain:float = '1'
 right_phase:bool = True 
 ...


HDCD_ANALYZE_MODE = Literal['off', 'lle', 'pe', 'cdt', 'tgm']
HDCD_BITS_PER_SAMPLE = Literal['16', '20', '24']

@dataclass
class hdcd(): # hdcd
 disable_autoconvert:bool = True
 process_stereo:bool = True
 cdt_ms:int = 2000
 force_pe:bool = False
 analyze_mode:HDCD_ANALYZE_MODE = 'off'
 bits_per_sample:HDCD_BITS_PER_SAMPLE = '16' 
 ...


HEADPHONE_TYPE = Literal['time', 'freq']
HEADPHONE_HRIR = Literal['stereo', 'multich']

@dataclass
class headphone(): # headphone
 map:str = None
 gain:float = '0'
 lfe:float = '0'
 type:HEADPHONE_TYPE = 'freq'
 size:int = 1024
 hrir:HEADPHONE_HRIR = 'stereo' 
 ...


HIGHPASS_WIDTH_TYPE = Literal['h', 'q', 'o', 's', 'k']
HIGHPASS_TRANSFORM = Literal['di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf']
HIGHPASS_PRECISION = Literal['auto', 's16', 's32', 'f32', 'f64']

@dataclass
class highpass(): # highpass
 frequency:float = '3000'
 f:float = '3000'
 width_type:HIGHPASS_WIDTH_TYPE = 'q'
 t:HIGHPASS_WIDTH_TYPE = 'q'
 width:float = '0.707'
 w:float = '0.707'
 poles:int = 2
 p:int = 2
 mix:float = '1'
 m:float = '1'
 channels:str = "all"
 c:str = "all"
 normalize:bool = False
 n:bool = False
 transform:HIGHPASS_TRANSFORM = 'di'
 a:HIGHPASS_TRANSFORM = 'di'
 precision:HIGHPASS_PRECISION = 'auto'
 r:HIGHPASS_PRECISION = 'auto'
 blocksize:int = 0
 b:int = 0 
 ...


TREBLE_HIGH_TILTSHELF_WIDTH_TYPE = Literal['h', 'q', 'o', 's', 'k']
TREBLE_HIGH_TILTSHELF_TRANSFORM = Literal['di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf']
TREBLE_HIGH_TILTSHELF_PRECISION = Literal['auto', 's16', 's32', 'f32', 'f64']

@dataclass
class treble_high_tiltshelf(): # treble/high/tiltshelf
 frequency:float = '3000'
 f:float = '3000'
 width_type:TREBLE_HIGH_TILTSHELF_WIDTH_TYPE = 'q'
 t:TREBLE_HIGH_TILTSHELF_WIDTH_TYPE = 'q'
 width:float = '0.5'
 w:float = '0.5'
 gain:float = '0'
 g:float = '0'
 poles:int = 2
 p:int = 2
 mix:float = '1'
 m:float = '1'
 channels:str = "all"
 c:str = "all"
 normalize:bool = False
 n:bool = False
 transform:TREBLE_HIGH_TILTSHELF_TRANSFORM = 'di'
 a:TREBLE_HIGH_TILTSHELF_TRANSFORM = 'di'
 precision:TREBLE_HIGH_TILTSHELF_PRECISION = 'auto'
 r:TREBLE_HIGH_TILTSHELF_PRECISION = 'auto'
 blocksize:int = 0
 b:int = 0 
 ...




@dataclass
class join(): # join
 inputs:int = 2
 channel_layout:str = "stereo"
 map:str = None 
 ...


LOUDNORM_PRINT_FORMAT = Literal['none', 'json', 'summary']

@dataclass
class loudnorm(): # loudnorm
 I:float = '-24'
 i:float = '-24'
 LRA:float = '7'
 lra:float = '7'
 TP:float = '-2'
 tp:float = '-2'
 measured_I:float = '0'
 measured_i:float = '0'
 measured_LRA:float = '0'
 measured_lra:float = '0'
 measured_TP:float = '99'
 measured_tp:float = '99'
 measured_thresh:float = '-70'
 offset:float = '0'
 linear:bool = True
 dual_mono:bool = False
 print_format:LOUDNORM_PRINT_FORMAT = 'none' 
 ...


LOWPASS_WIDTH_TYPE = Literal['h', 'q', 'o', 's', 'k']
LOWPASS_TRANSFORM = Literal['di', 'dii', 'tdi', 'tdii', 'latt', 'svf', 'zdf']
LOWPASS_PRECISION = Literal['auto', 's16', 's32', 'f32', 'f64']

@dataclass
class lowpass(): # lowpass
 frequency:float = '500'
 f:float = '500'
 width_type:LOWPASS_WIDTH_TYPE = 'q'
 t:LOWPASS_WIDTH_TYPE = 'q'
 width:float = '0.707'
 w:float = '0.707'
 poles:int = 2
 p:int = 2
 mix:float = '1'
 m:float = '1'
 channels:str = "all"
 c:str = "all"
 normalize:bool = False
 n:bool = False
 transform:LOWPASS_TRANSFORM = 'di'
 a:LOWPASS_TRANSFORM = 'di'
 precision:LOWPASS_PRECISION = 'auto'
 r:LOWPASS_PRECISION = 'auto'
 blocksize:int = 0
 b:int = 0 
 ...




@dataclass
class mcompand(): # mcompand
 args:str = "0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000" 
 ...




@dataclass
class pan(): # pan
 args:str = None 
 ...


RUBBERBAND_TRANSIENTS = Literal['crisp', 'mixed', 'smooth']
RUBBERBAND_DETECTOR = Literal['compound', 'percussive', 'soft']
RUBBERBAND_PHASE = Literal['laminar', 'independent']
RUBBERBAND_WINDOW = Literal['standard', 'short', 'long']
RUBBERBAND_SMOOTHING = Literal['off', 'on']
RUBBERBAND_FORMANT = Literal['shifted', 'preserved']
RUBBERBAND_PITCHQ = Literal['quality', 'speed', 'consistency']
RUBBERBAND_CHANNELS = Literal['apart', 'together']

@dataclass
class rubberband(): # rubberband
 tempo:float = '1'
 pitch:float = '1'
 transients:RUBBERBAND_TRANSIENTS = 'crisp'
 detector:RUBBERBAND_DETECTOR = 'compound'
 phase:RUBBERBAND_PHASE = 'laminar'
 window:RUBBERBAND_WINDOW = 'standard'
 smoothing:RUBBERBAND_SMOOTHING = 'off'
 formant:RUBBERBAND_FORMANT = 'shifted'
 pitchq:RUBBERBAND_PITCHQ = 'speed'
 channels:RUBBERBAND_CHANNELS = 'apart' 
 ...




@dataclass
class silencedetect(): # silencedetect
 n:float = '0.001'
 noise:float = '0.001'
 d:str = '2'
 duration:str = '2'
 mono:bool = False
 m:bool = False 
 ...


SILENCEREMOVE_START_MODE = Literal['any', 'all']
SILENCEREMOVE_DETECTION = Literal['peak', 'rms']

@dataclass
class silenceremove(): # silenceremove
 start_periods:int = 0
 start_duration:str = '0'
 start_threshold:float = '0'
 start_silence:str = '0'
 start_mode:SILENCEREMOVE_START_MODE = 'any'
 stop_periods:int = 0
 stop_duration:str = '0'
 stop_threshold:float = '0'
 stop_silence:str = '0'
 stop_mode:SILENCEREMOVE_START_MODE = 'any'
 detection:SILENCEREMOVE_DETECTION = 'rms'
 window:str = '0.02' 
 ...




@dataclass
class speechnorm(): # speechnorm
 peak:float = '0.95'
 p:float = '0.95'
 expansion:float = '2'
 e:float = '2'
 compression:float = '2'
 c:float = '2'
 threshold:float = '0'
 t:float = '0'
 _raise:float = dataclasses_field(default='0.001', metadata='raise')
 r:float = '0.001'
 fall:float = '0.001'
 f:float = '0.001'
 channels:str = "all"
 h:str = "all"
 invert:bool = False
 i:bool = False
 link:bool = False
 l:bool = False
 rms:float = '0'
 m:float = '0' 
 ...


STEREOTOOLS_MODE = Literal['lr>lr', 'lr>ms', 'ms>lr', 'lr>ll', 'lr>rr', 'lr>l+r', 'lr>rl', 'ms>ll', 'ms>rr', 'ms>rl', 'lr>l-r']
STEREOTOOLS_BMODE_IN = Literal['balance', 'amplitude', 'power']

@dataclass
class stereotools(): # stereotools
 level_in:float = '1'
 level_out:float = '1'
 balance_in:float = '0'
 balance_out:float = '0'
 softclip:bool = False
 mutel:bool = False
 muter:bool = False
 phasel:bool = False
 phaser:bool = False
 mode:STEREOTOOLS_MODE = 'lr>lr'
 slev:float = '1'
 sbal:float = '0'
 mlev:float = '1'
 mpan:float = '0'
 base:float = '0'
 delay:float = '0'
 sclevel:float = '1'
 phase:float = '0'
 bmode_in:STEREOTOOLS_BMODE_IN = 'balance'
 bmode_out:STEREOTOOLS_BMODE_IN = 'balance' 
 ...




@dataclass
class stereowiden(): # stereowiden
 delay:float = '20'
 feedback:float = '0.3'
 crossfeed:float = '0.3'
 drymix:float = '0.8' 
 ...




@dataclass
class superequalizer(): # superequalizer
 _1b:float = dataclasses_field(default='1', metadata='1b')
 _2b:float = dataclasses_field(default='1', metadata='2b')
 _3b:float = dataclasses_field(default='1', metadata='3b')
 _4b:float = dataclasses_field(default='1', metadata='4b')
 _5b:float = dataclasses_field(default='1', metadata='5b')
 _6b:float = dataclasses_field(default='1', metadata='6b')
 _7b:float = dataclasses_field(default='1', metadata='7b')
 _8b:float = dataclasses_field(default='1', metadata='8b')
 _9b:float = dataclasses_field(default='1', metadata='9b')
 _10b:float = dataclasses_field(default='1', metadata='10b')
 _11b:float = dataclasses_field(default='1', metadata='11b')
 _12b:float = dataclasses_field(default='1', metadata='12b')
 _13b:float = dataclasses_field(default='1', metadata='13b')
 _14b:float = dataclasses_field(default='1', metadata='14b')
 _15b:float = dataclasses_field(default='1', metadata='15b')
 _16b:float = dataclasses_field(default='1', metadata='16b')
 _17b:float = dataclasses_field(default='1', metadata='17b')
 _18b:float = dataclasses_field(default='1', metadata='18b') 
 ...


SURROUND_LFE_MODE = Literal['add', 'sub']
SURROUND_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']

@dataclass
class surround(): # surround
 chl_out:str = "5.1"
 chl_in:str = "stereo"
 level_in:float = '1'
 level_out:float = '1'
 lfe:bool = True
 lfe_low:int = 128
 lfe_high:int = 256
 lfe_mode:SURROUND_LFE_MODE = 'add'
 smooth:float = '0'
 angle:float = '90'
 focus:float = '0'
 fc_in:float = '1'
 fc_out:float = '1'
 fl_in:float = '1'
 fl_out:float = '1'
 fr_in:float = '1'
 fr_out:float = '1'
 sl_in:float = '1'
 sl_out:float = '1'
 sr_in:float = '1'
 sr_out:float = '1'
 bl_in:float = '1'
 bl_out:float = '1'
 br_in:float = '1'
 br_out:float = '1'
 bc_in:float = '1'
 bc_out:float = '1'
 lfe_in:float = '1'
 lfe_out:float = '1'
 allx:float = '-1'
 ally:float = '-1'
 fcx:float = '0.5'
 flx:float = '0.5'
 frx:float = '0.5'
 blx:float = '0.5'
 brx:float = '0.5'
 slx:float = '0.5'
 srx:float = '0.5'
 bcx:float = '0.5'
 fcy:float = '0.5'
 fly:float = '0.5'
 fry:float = '0.5'
 bly:float = '0.5'
 bry:float = '0.5'
 sly:float = '0.5'
 sry:float = '0.5'
 bcy:float = '0.5'
 win_size:int = 4096
 win_func:SURROUND_WIN_FUNC = 'hann'
 overlap:float = '0.5' 
 ...




@dataclass
class tremolo(): # tremolo
 f:float = '5'
 d:float = '0.5' 
 ...




@dataclass
class vibrato(): # vibrato
 f:float = '5'
 d:float = '0.5' 
 ...




@dataclass
class virtualbass(): # virtualbass
 cutoff:float = '250'
 strength:float = '3' 
 ...


VOLUME_PRECISION = Literal['fixed', 'float', 'double']
VOLUME_EVAL = Literal['once', 'frame']
VOLUME_REPLAYGAIN = Literal['drop', 'ignore', 'track', 'album']

@dataclass
class volume(): # volume
 volume:str = "1.0"
 precision:VOLUME_PRECISION = 'float'
 eval:VOLUME_EVAL = 'once'
 replaygain:VOLUME_REPLAYGAIN = 'drop'
 replaygain_preamp:float = '0'
 replaygain_noclip:bool = True 
 ...




@dataclass
class aevalsrc(): # aevalsrc
 exprs:str = None
 nb_samples:int = 1024
 n:int = 1024
 sample_rate:str = "44100"
 s:str = "44100"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 channel_layout:str = None
 c:str = None 
 ...




@dataclass
class afdelaysrc(): # afdelaysrc
 delay:float = '0'
 d:float = '0'
 sample_rate:int = 44100
 r:int = 44100
 nb_samples:int = 1024
 n:int = 1024
 taps:int = 0
 t:int = 0
 channel_layout:str = "stereo"
 c:str = "stereo" 
 ...


AFIRSRC_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser', 'rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']

@dataclass
class afirsrc(): # afirsrc
 taps:int = 1025
 t:int = 1025
 frequency:str = "0 1"
 f:str = "0 1"
 magnitude:str = "1 1"
 m:str = "1 1"
 phase:str = "0 0"
 p:str = "0 0"
 sample_rate:int = 44100
 r:int = 44100
 nb_samples:int = 1024
 n:int = 1024
 win_func:AFIRSRC_WIN_FUNC = 'blackman'
 w:AFIRSRC_WIN_FUNC = 'blackman' 
 ...


ANOISESRC_COLOR = Literal['white', 'pink', 'brown', 'blue', 'violet', 'velvet']

@dataclass
class anoisesrc(): # anoisesrc
 sample_rate:int = 48000
 r:int = 48000
 amplitude:float = '1'
 a:float = '1'
 duration:str = '0'
 d:str = '0'
 color:ANOISESRC_COLOR = 'white'
 colour:ANOISESRC_COLOR = 'white'
 c:ANOISESRC_COLOR = 'white'
 seed:int = -1
 s:int = -1
 nb_samples:int = 1024
 n:int = 1024 
 ...




@dataclass
class anullsrc(): # anullsrc
 channel_layout:str = "stereo"
 cl:str = "stereo"
 sample_rate:str = "44100"
 r:str = "44100"
 nb_samples:int = 1024
 n:int = 1024
 duration:str = '-0.000001'
 d:str = '-0.000001' 
 ...


HILBERT_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser', 'rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']

@dataclass
class hilbert(): # hilbert
 sample_rate:int = 44100
 r:int = 44100
 taps:int = 22051
 t:int = 22051
 nb_samples:int = 1024
 n:int = 1024
 win_func:HILBERT_WIN_FUNC = 'blackman'
 w:HILBERT_WIN_FUNC = 'blackman' 
 ...




@dataclass
class sinc(): # sinc
 sample_rate:int = 44100
 r:int = 44100
 nb_samples:int = 1024
 n:int = 1024
 hp:float = '0'
 lp:float = '0'
 phase:float = '50'
 beta:float = '-1'
 att:float = '120'
 round:bool = False
 hptaps:int = 0
 lptaps:int = 0 
 ...




@dataclass
class sine(): # sine
 frequency:float = '440'
 f:float = '440'
 beep_factor:float = '0'
 b:float = '0'
 sample_rate:int = 44100
 r:int = 44100
 duration:str = '0'
 d:str = '0'
 samples_per_frame:str = "1024" 
 ...




@dataclass
class addroi(): # addroi
 x:str = "0"
 y:str = "0"
 w:str = "0"
 h:str = "0"
 qoffset:float|str = '-1/10'
 clear:bool = False 
 ...




@dataclass
class alphamerge(): # alphamerge 
 ...


FRAMESYNC_EOF_ACTION = Literal['repeat', 'endall', 'pass']
FRAMESYNC_TS_SYNC_MODE = Literal['default', 'nearest']

@dataclass
class framesync(): # framesync
 eof_action:FRAMESYNC_EOF_ACTION = 'repeat'
 shortest:bool = False
 repeatlast:bool = True
 ts_sync_mode:FRAMESYNC_TS_SYNC_MODE = 'default' 
 ...




@dataclass
class amplify(): # amplify
 radius:int = 2
 factor:float = '2'
 threshold:float = '10'
 tolerance:float = '0'
 low:float = '65535'
 high:float = '65535'
 planes:str = '7' 
 ...


ASS_SHAPING = Literal['auto', 'simple', 'complex']

@dataclass
class ass(): # ass
 filename:str = None
 f:str = None
 original_size:IMAGE_SIZES = None
 fontsdir:str = None
 alpha:bool = False
 shaping:ASS_SHAPING = 'auto' 
 ...


ATADENOISE_A = Literal['p', 's']

@dataclass
class atadenoise(): # atadenoise
 _0a:float = dataclasses_field(default='0.02', metadata='0a')
 _0b:float = dataclasses_field(default='0.04', metadata='0b')
 _1a:float = dataclasses_field(default='0.02', metadata='1a')
 _1b:float = dataclasses_field(default='0.04', metadata='1b')
 _2a:float = dataclasses_field(default='0.02', metadata='2a')
 _2b:float = dataclasses_field(default='0.04', metadata='2b')
 s:int = 9
 p:str = '7'
 a:ATADENOISE_A = 'p'
 _0s:float = dataclasses_field(default='32767', metadata='0s')
 _1s:float = dataclasses_field(default='32767', metadata='1s')
 _2s:float = dataclasses_field(default='32767', metadata='2s') 
 ...




@dataclass
class avgblur(): # avgblur
 sizeX:int = 1
 planes:int = 15
 sizeY:int = 0 
 ...




@dataclass
class backgroundkey(): # backgroundkey
 threshold:float = '0.08'
 similarity:float = '0.1'
 blend:float = '0' 
 ...




@dataclass
class bbox(): # bbox
 min_val:int = 16 
 ...


BENCH_ACTION = Literal['start', 'stop']

@dataclass
class bench(): # bench
 action:BENCH_ACTION = 'start' 
 ...




@dataclass
class bilateral(): # bilateral
 sigmaS:float = '0.1'
 sigmaR:float = '0.1'
 planes:int = 1 
 ...




@dataclass
class bitplanenoise(): # bitplanenoise
 bitplane:int = 1
 filter:bool = False 
 ...




@dataclass
class blackdetect(): # blackdetect
 d:float = '2'
 black_min_duration:float = '2'
 picture_black_ratio_th:float = '0.98'
 pic_th:float = '0.98'
 pixel_black_th:float = '0.1'
 pix_th:float = '0.1' 
 ...




@dataclass
class blackframe(): # blackframe
 amount:int = 98
 threshold:int = 32
 thresh:int = 32 
 ...


BLEND_C0_MODE = Literal['addition', 'addition128', 'grainmerge', 'and', 'average', 'burn', 'darken', 'difference', 'difference128', 'grainextract', 'divide', 'dodge', 'exclusion', 'extremity', 'freeze', 'glow', 'hardlight', 'hardmix', 'heat', 'lighten', 'linearlight', 'multiply', 'multiply128', 'negation', 'normal', 'or', 'overlay', 'phoenix', 'pinlight', 'reflect', 'screen', 'softlight', 'subtract', 'vividlight', 'xor', 'softdifference', 'geometric', 'harmonic', 'bleach', 'stain', 'interpolate', 'hardoverlay']

@dataclass
class blend(): # blend
 c0_mode:BLEND_C0_MODE = 'normal'
 c1_mode:BLEND_C0_MODE = 'normal'
 c2_mode:BLEND_C0_MODE = 'normal'
 c3_mode:BLEND_C0_MODE = 'normal'
 all_mode:BLEND_C0_MODE = '-1'
 c0_expr:str = None
 c1_expr:str = None
 c2_expr:str = None
 c3_expr:str = None
 all_expr:str = None
 c0_opacity:float = '1'
 c1_opacity:float = '1'
 c2_opacity:float = '1'
 c3_opacity:float = '1'
 all_opacity:float = '1' 
 ...




@dataclass
class blockdetect(): # blockdetect
 period_min:int = 3
 period_max:int = 24
 planes:int = 1 
 ...




@dataclass
class blurdetect(): # blurdetect
 high:float = '0.117647'
 low:float = '0.0588235'
 radius:int = 50
 block_pct:int = 80
 block_width:int = -1
 block_height:int = -1
 planes:int = 1 
 ...


BM3D_ESTIM = Literal['basic', 'final']

@dataclass
class bm3d(): # bm3d
 sigma:float = '1'
 block:int = 16
 bstep:int = 4
 group:int = 1
 range:int = 9
 mstep:int = 1
 thmse:float = '0'
 hdthr:float = '2.7'
 estim:BM3D_ESTIM = 'basic'
 ref:bool = False
 planes:int = 7 
 ...




@dataclass
class boxblur(): # boxblur
 luma_radius:str = "2"
 lr:str = "2"
 luma_power:int = 2
 lp:int = 2
 chroma_radius:str = None
 cr:str = None
 chroma_power:int = -1
 cp:int = -1
 alpha_radius:str = None
 ar:str = None
 alpha_power:int = -1
 ap:int = -1 
 ...


BWDIF_MODE = Literal['send_frame', 'send_field']
BWDIF_PARITY = Literal['tff', 'bff', 'auto']
BWDIF_DEINT = Literal['all', 'interlaced']

@dataclass
class bwdif(): # bwdif
 mode:BWDIF_MODE = 'send_field'
 parity:BWDIF_PARITY = 'auto'
 deint:BWDIF_DEINT = 'all' 
 ...




@dataclass
class cas(): # cas
 strength:float = '0'
 planes:str = '7' 
 ...




@dataclass
class chromahold(): # chromahold
 color:COLORS = "black"
 similarity:float = '0.01'
 blend:float = '0'
 yuv:bool = False 
 ...




@dataclass
class chromakey(): # chromakey
 color:COLORS = "black"
 similarity:float = '0.01'
 blend:float = '0'
 yuv:bool = False 
 ...


CHROMANR_DISTANCE = Literal['manhattan', 'euclidean']

@dataclass
class chromanr(): # chromanr
 thres:float = '30'
 sizew:int = 5
 sizeh:int = 5
 stepw:int = 1
 steph:int = 1
 threy:float = '200'
 threu:float = '200'
 threv:float = '200'
 distance:CHROMANR_DISTANCE = 'manhattan' 
 ...


CHROMASHIFT_EDGE = Literal['smear', 'wrap']

@dataclass
class chromashift(): # chromashift
 cbh:int = 0
 cbv:int = 0
 crh:int = 0
 crv:int = 0
 edge:CHROMASHIFT_EDGE = 'smear' 
 ...


CIESCOPE_SYSTEM = Literal['ntsc', '470m', 'ebu', '470bg', 'smpte', '240m', 'apple', 'widergb', 'cie1931', 'hdtv', 'rec709', 'uhdtv', 'rec2020', 'dcip3']
CIESCOPE_CIE = Literal['xyy', 'ucs', 'luv']

@dataclass
class ciescope(): # ciescope
 system:CIESCOPE_SYSTEM = 'hdtv'
 cie:CIESCOPE_CIE = 'xyy'
 gamuts:CIESCOPE_SYSTEM = '0'
 size:int = 512
 s:int = 512
 intensity:float = '0.001'
 i:float = '0.001'
 contrast:float = '0.75'
 corrgamma:bool = True
 showwhite:bool = False
 gamma:float = '2.6'
 fill:bool = True 
 ...


CODECVIEW_MV = Literal['pf', 'bf', 'bb']
CODECVIEW_MV_TYPE = Literal['fp', 'bp']
CODECVIEW_FRAME_TYPE = Literal['if', 'pf', 'bf']

@dataclass
class codecview(): # codecview
 mv:CODECVIEW_MV = '0'
 qp:bool = False
 mv_type:CODECVIEW_MV_TYPE = '0'
 mvt:CODECVIEW_MV_TYPE = '0'
 frame_type:CODECVIEW_FRAME_TYPE = '0'
 ft:CODECVIEW_FRAME_TYPE = '0'
 block:bool = False 
 ...




@dataclass
class colorbalance(): # colorbalance
 rs:float = '0'
 gs:float = '0'
 bs:float = '0'
 rm:float = '0'
 gm:float = '0'
 bm:float = '0'
 rh:float = '0'
 gh:float = '0'
 bh:float = '0'
 pl:bool = False 
 ...


COLORCHANNELMIXER_PC = Literal['none', 'lum', 'max', 'avg', 'sum', 'nrm', 'pwr']

@dataclass
class colorchannelmixer(): # colorchannelmixer
 rr:float = '1'
 rg:float = '0'
 rb:float = '0'
 ra:float = '0'
 gr:float = '0'
 gg:float = '1'
 gb:float = '0'
 ga:float = '0'
 br:float = '0'
 bg:float = '0'
 bb:float = '1'
 ba:float = '0'
 ar:float = '0'
 ag:float = '0'
 ab:float = '0'
 aa:float = '1'
 pc:COLORCHANNELMIXER_PC = 'none'
 pa:float = '0' 
 ...




@dataclass
class colorcontrast(): # colorcontrast
 rc:float = '0'
 gm:float = '0'
 by:float = '0'
 rcw:float = '0'
 gmw:float = '0'
 byw:float = '0'
 pl:float = '0' 
 ...


COLORCORRECT_ANALYZE = Literal['manual', 'average', 'minmax', 'median']

@dataclass
class colorcorrect(): # colorcorrect
 rl:float = '0'
 bl:float = '0'
 rh:float = '0'
 bh:float = '0'
 saturation:float = '1'
 analyze:COLORCORRECT_ANALYZE = 'manual' 
 ...




@dataclass
class colorize(): # colorize
 hue:float = '0'
 saturation:float = '0.5'
 lightness:float = '0.5'
 mix:float = '1' 
 ...




@dataclass
class colorkey(): # colorkey
 color:COLORS = "black"
 similarity:float = '0.01'
 blend:float = '0' 
 ...




@dataclass
class colorhold(): # colorhold
 color:COLORS = "black"
 similarity:float = '0.01'
 blend:float = '0' 
 ...


COLORLEVELS_PRESERVE = Literal['none', 'lum', 'max', 'avg', 'sum', 'nrm', 'pwr']

@dataclass
class colorlevels(): # colorlevels
 rimin:float = '0'
 gimin:float = '0'
 bimin:float = '0'
 aimin:float = '0'
 rimax:float = '1'
 gimax:float = '1'
 bimax:float = '1'
 aimax:float = '1'
 romin:float = '0'
 gomin:float = '0'
 bomin:float = '0'
 aomin:float = '0'
 romax:float = '1'
 gomax:float = '1'
 bomax:float = '1'
 aomax:float = '1'
 preserve:COLORLEVELS_PRESERVE = 'none' 
 ...


COLORMAP_TYPE = Literal['relative', 'absolute']
COLORMAP_KERNEL = Literal['euclidean', 'weuclidean']

@dataclass
class colormap(): # colormap
 patch_size:IMAGE_SIZES = "64x64"
 nb_patches:int = 0
 type:COLORMAP_TYPE = 'absolute'
 kernel:COLORMAP_KERNEL = 'euclidean' 
 ...


COLORMATRIX_SRC = Literal['bt709', 'fcc', 'bt601', 'bt470', 'bt470bg', 'smpte170m', 'smpte240m', 'bt2020']

@dataclass
class colormatrix(): # colormatrix
 src:COLORMATRIX_SRC = '-1'
 dst:COLORMATRIX_SRC = '-1' 
 ...


COLORSPACE_ALL = Literal['bt470m', 'bt470bg', 'bt601-6-525', 'bt601-6-625', 'bt709', 'smpte170m', 'smpte240m', 'bt2020']
COLORSPACE_SPACE = Literal['bt709', 'fcc', 'bt470bg', 'smpte170m', 'smpte240m', 'ycgco', 'gbr', 'bt2020nc', 'bt2020ncl']
COLORSPACE_RANGE = Literal['tv', 'mpeg', 'pc', 'jpeg']
COLORSPACE_PRIMARIES = Literal['bt709', 'bt470m', 'bt470bg', 'smpte170m', 'smpte240m', 'smpte428', 'film', 'smpte431', 'smpte432', 'bt2020', 'jedec-p22', 'ebu3213']
COLORSPACE_TRC = Literal['bt709', 'bt470m', 'gamma22', 'bt470bg', 'gamma28', 'smpte170m', 'smpte240m', 'linear', 'srgb', 'iec61966-2-1', 'xvycc', 'iec61966-2-4', 'bt2020-10', 'bt2020-12']
COLORSPACE_FORMAT = Literal['yuv420p', 'yuv420p10', 'yuv420p12', 'yuv422p', 'yuv422p10', 'yuv422p12', 'yuv444p', 'yuv444p10', 'yuv444p12']
COLORSPACE_DITHER = Literal['none', 'fsb']
COLORSPACE_WPADAPT = Literal['bradford', 'vonkries', 'identity']

@dataclass
class colorspace(): # colorspace
 all:COLORSPACE_ALL = '0'
 space:COLORSPACE_SPACE = '2'
 range:COLORSPACE_RANGE = '0'
 primaries:COLORSPACE_PRIMARIES = '2'
 trc:COLORSPACE_TRC = '2'
 format:COLORSPACE_FORMAT = '-1'
 fast:bool = False
 dither:COLORSPACE_DITHER = 'none'
 wpadapt:COLORSPACE_WPADAPT = 'bradford'
 iall:COLORSPACE_ALL = '0'
 ispace:COLORSPACE_SPACE = '2'
 irange:COLORSPACE_RANGE = '0'
 iprimaries:COLORSPACE_PRIMARIES = '2'
 itrc:COLORSPACE_TRC = '2' 
 ...




@dataclass
class colortemperature(): # colortemperature
 temperature:float = '6500'
 mix:float = '1'
 pl:float = '0' 
 ...


CONVOLUTION__0MODE = Literal['square', 'row', 'column']

@dataclass
class convolution(): # convolution
 _0m:str = dataclasses_field(default="0 0 0 0 1 0 0 0 0", metadata='0m')
 _1m:str = dataclasses_field(default="0 0 0 0 1 0 0 0 0", metadata='1m')
 _2m:str = dataclasses_field(default="0 0 0 0 1 0 0 0 0", metadata='2m')
 _3m:str = dataclasses_field(default="0 0 0 0 1 0 0 0 0", metadata='3m')
 _0rdiv:float = dataclasses_field(default='0', metadata='0rdiv')
 _1rdiv:float = dataclasses_field(default='0', metadata='1rdiv')
 _2rdiv:float = dataclasses_field(default='0', metadata='2rdiv')
 _3rdiv:float = dataclasses_field(default='0', metadata='3rdiv')
 _0bias:float = dataclasses_field(default='0', metadata='0bias')
 _1bias:float = dataclasses_field(default='0', metadata='1bias')
 _2bias:float = dataclasses_field(default='0', metadata='2bias')
 _3bias:float = dataclasses_field(default='0', metadata='3bias')
 _0mode:CONVOLUTION__0MODE = dataclasses_field(default='square', metadata='0mode')
 _1mode:CONVOLUTION__0MODE = dataclasses_field(default='square', metadata='1mode')
 _2mode:CONVOLUTION__0MODE = dataclasses_field(default='square', metadata='2mode')
 _3mode:CONVOLUTION__0MODE = dataclasses_field(default='square', metadata='3mode') 
 ...


CONVOLVE_IMPULSE = Literal['first', 'all']

@dataclass
class convolve(): # convolve
 planes:int = 7
 impulse:CONVOLVE_IMPULSE = 'all'
 noise:float = '1e-07' 
 ...




@dataclass
class coreimage(): # coreimage
 list_filters:bool = False
 list_generators:bool = False
 filter:str = None
 output_rect:str = None 
 ...




@dataclass
class corr(): # corr 
 ...


COVER_RECT_MODE = Literal['cover', 'blur']

@dataclass
class cover_rect(): # cover_rect
 cover:str = None
 mode:COVER_RECT_MODE = 'blur' 
 ...




@dataclass
class crop(): # crop
 out_w:str = "iw"
 w:str = "iw"
 out_h:str = "ih"
 h:str = "ih"
 x:str = None
 y:str = None
 keep_aspect:bool = False
 exact:bool = False 
 ...


CROPDETECT_MODE = Literal['black', 'mvedges']

@dataclass
class cropdetect(): # cropdetect
 limit:float = '0.0941176'
 round:int = 16
 reset:int = 0
 skip:int = 2
 reset_count:int = 0
 max_outliers:int = 0
 mode:CROPDETECT_MODE = 'black'
 high:float = '0.0980392'
 low:float = '0.0588235'
 mv_threshold:int = 8 
 ...


CURVES_PRESET = Literal['none', 'color_negative', 'cross_process', 'darker', 'increase_contrast', 'lighter', 'linear_contrast', 'medium_contrast', 'negative', 'strong_contrast', 'vintage']
CURVES_INTERP = Literal['natural', 'pchip']

@dataclass
class curves(): # curves
 preset:CURVES_PRESET = 'none'
 master:str = None
 m:str = None
 red:str = None
 r:str = None
 green:str = None
 g:str = None
 blue:str = None
 b:str = None
 all:str = None
 psfile:str = None
 plot:str = None
 interp:CURVES_INTERP = 'natural' 
 ...


DATASCOPE_MODE = Literal['mono', 'color', 'color2']
DATASCOPE_FORMAT = Literal['hex', 'dec']

@dataclass
class datascope(): # datascope
 size:IMAGE_SIZES = "hd720"
 s:IMAGE_SIZES = "hd720"
 x:int = 0
 y:int = 0
 mode:DATASCOPE_MODE = 'mono'
 axis:bool = False
 opacity:float = '0.75'
 format:DATASCOPE_FORMAT = 'hex'
 components:int = 15 
 ...




@dataclass
class dblur(): # dblur
 angle:float = '45'
 radius:float = '5'
 planes:int = 15 
 ...




@dataclass
class dctdnoiz(): # dctdnoiz
 sigma:float = '0'
 s:float = '0'
 overlap:int = -1
 expr:str = None
 e:str = None
 n:int = 3 
 ...




@dataclass
class deband(): # deband
 _1thr:float = dataclasses_field(default='0.02', metadata='1thr')
 _2thr:float = dataclasses_field(default='0.02', metadata='2thr')
 _3thr:float = dataclasses_field(default='0.02', metadata='3thr')
 _4thr:float = dataclasses_field(default='0.02', metadata='4thr')
 range:int = 16
 r:int = 16
 direction:float = '6.28319'
 d:float = '6.28319'
 blur:bool = True
 b:bool = True
 coupling:bool = False
 c:bool = False 
 ...


DEBLOCK_FILTER = Literal['weak', 'strong']

@dataclass
class deblock(): # deblock
 filter:DEBLOCK_FILTER = 'strong'
 block:int = 8
 alpha:float = '0.098'
 beta:float = '0.05'
 gamma:float = '0.05'
 delta:float = '0.05'
 planes:int = 15 
 ...




@dataclass
class decimate(): # decimate
 cycle:int = 5
 dupthresh:float = '1.1'
 scthresh:float = '15'
 blockx:int = 32
 blocky:int = 32
 ppsrc:bool = False
 chroma:bool = True
 mixed:bool = False 
 ...


DECONVOLVE_IMPULSE = Literal['first', 'all']

@dataclass
class deconvolve(): # deconvolve
 planes:int = 7
 impulse:DECONVOLVE_IMPULSE = 'all'
 noise:float = '1e-07' 
 ...


DEDOT_M = Literal['dotcrawl', 'rainbows']

@dataclass
class dedot(): # dedot
 m:DEDOT_M = 'dotcrawl+rainbows'
 lt:float = '0.079'
 tl:float = '0.079'
 tc:float = '0.058'
 ct:float = '0.019' 
 ...




@dataclass
class deflate_inflate(): # deflate/inflate
 threshold0:int = 65535
 threshold1:int = 65535
 threshold2:int = 65535
 threshold3:int = 65535 
 ...


DEFLICKER_MODE = Literal['am', 'gm', 'hm', 'qm', 'cm', 'pm', 'median']

@dataclass
class deflicker(): # deflicker
 size:int = 5
 s:int = 5
 mode:DEFLICKER_MODE = 'am'
 m:DEFLICKER_MODE = 'am'
 bypass:bool = False 
 ...




@dataclass
class dejudder(): # dejudder
 cycle:int = 4 
 ...




@dataclass
class delogo(): # delogo
 x:str = "-1"
 y:str = "-1"
 w:str = "-1"
 h:str = "-1"
 show:bool = False 
 ...


DERAIN_FILTER_TYPE = Literal['derain', 'dehaze']
DERAIN_DNN_BACKEND = Literal['native']

@dataclass
class derain(): # derain
 filter_type:DERAIN_FILTER_TYPE = 'derain'
 dnn_backend:DERAIN_DNN_BACKEND = 'native'
 model:str = None
 input:str = "x"
 output:str = "y" 
 ...


DESHAKE_EDGE = Literal['blank', 'original', 'clamp', 'mirror']
DESHAKE_SEARCH = Literal['exhaustive', 'less']

@dataclass
class deshake(): # deshake
 x:int = -1
 y:int = -1
 w:int = -1
 h:int = -1
 rx:int = 16
 ry:int = 16
 edge:DESHAKE_EDGE = 'mirror'
 blocksize:int = 8
 contrast:int = 125
 search:DESHAKE_SEARCH = 'exhaustive'
 filename:str = None
 opencl:bool = False 
 ...


DESPILL_TYPE = Literal['green', 'blue']

@dataclass
class despill(): # despill
 type:DESPILL_TYPE = 'green'
 mix:float = '0.5'
 expand:float = '0'
 red:float = '0'
 green:float = '-1'
 blue:float = '0'
 brightness:float = '0'
 alpha:bool = False 
 ...


DETELECINE_FIRST_FIELD = Literal['top', 't', 'bottom', 'b']

@dataclass
class detelecine(): # detelecine
 first_field:DETELECINE_FIRST_FIELD = 'top'
 pattern:str = "23"
 start_frame:int = 0 
 ...




@dataclass
class erosion_dilation(): # erosion/dilation
 coordinates:int = 255
 threshold0:int = 65535
 threshold1:int = 65535
 threshold2:int = 65535
 threshold3:int = 65535 
 ...


DISPLACE_EDGE = Literal['blank', 'smear', 'wrap', 'mirror']

@dataclass
class displace(): # displace
 edge:DISPLACE_EDGE = 'smear' 
 ...




@dataclass
class dnn_classify(): # dnn_classify
 dnn_backend:int = 2
 model:str = None
 input:str = None
 output:str = None
 backend_configs:str = None
 options:str = None
 _async:bool = dataclasses_field(default=True, metadata='async')
 confidence:float = '0.5'
 labels:str = None
 target:str = None 
 ...




@dataclass
class dnn_detect(): # dnn_detect
 dnn_backend:int = 2
 model:str = None
 input:str = None
 output:str = None
 backend_configs:str = None
 options:str = None
 _async:bool = dataclasses_field(default=True, metadata='async')
 confidence:float = '0.5'
 labels:str = None 
 ...


DNN_PROCESSING_DNN_BACKEND = Literal['native']

@dataclass
class dnn_processing(): # dnn_processing
 dnn_backend:DNN_PROCESSING_DNN_BACKEND = 'native'
 model:str = None
 input:str = None
 output:str = None
 backend_configs:str = None
 options:str = None
 _async:bool = dataclasses_field(default=True, metadata='async') 
 ...


_DOUBLE_WEAVE_FIRST_FIELD = Literal['top', 't', 'bottom', 'b']

@dataclass
class _double_weave(): # (double)weave
 first_field:_DOUBLE_WEAVE_FIRST_FIELD = 'top' 
 ...




@dataclass
class drawbox(): # drawbox
 x:str = "0"
 y:str = "0"
 width:str = "0"
 w:str = "0"
 height:str = "0"
 h:str = "0"
 color:str = "black"
 c:str = "black"
 thickness:str = "3"
 t:str = "3"
 replace:bool = False
 box_source:str = None 
 ...


_A_DRAWGRAPH_MODE = Literal['bar', 'dot', 'line']
_A_DRAWGRAPH_SLIDE = Literal['frame', 'replace', 'scroll', 'rscroll', 'picture']

@dataclass
class _a_drawgraph(): # (a)drawgraph
 m1:str = ""
 fg1:str = "0xffff0000"
 m2:str = ""
 fg2:str = "0xff00ff00"
 m3:str = ""
 fg3:str = "0xffff00ff"
 m4:str = ""
 fg4:str = "0xffffff00"
 bg:COLORS = "white"
 min:float = '-1'
 max:float = '1'
 mode:_A_DRAWGRAPH_MODE = 'line'
 slide:_A_DRAWGRAPH_SLIDE = 'frame'
 size:IMAGE_SIZES = "900x256"
 s:IMAGE_SIZES = "900x256"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25" 
 ...




@dataclass
class drawgrid(): # drawgrid
 x:str = "0"
 y:str = "0"
 width:str = "0"
 w:str = "0"
 height:str = "0"
 h:str = "0"
 color:str = "black"
 c:str = "black"
 thickness:str = "1"
 t:str = "1"
 replace:bool = False 
 ...


DRAWTEXT_EXPANSION = Literal['none', 'normal', 'strftime']
DRAWTEXT_FT_LOAD_FLAGS = Literal['default', 'no_scale', 'no_hinting', 'render', 'no_bitmap', 'vertical_layout', 'force_autohint', 'crop_bitmap', 'pedantic', 'ignore_global_advance_width', 'no_recurse', 'ignore_transform', 'monochrome', 'linear_design', 'no_autohint']

@dataclass
class drawtext(): # drawtext
 fontfile:str = None
 text:str = None
 textfile:str = None
 fontcolor:COLORS = "black"
 fontcolor_expr:str = ""
 boxcolor:COLORS = "white"
 bordercolor:COLORS = "black"
 shadowcolor:COLORS = "black"
 box:bool = False
 boxborderw:int = 0
 line_spacing:int = 0
 fontsize:str = None
 x:str = "0"
 y:str = "0"
 shadowx:int = 0
 shadowy:int = 0
 borderw:int = 0
 tabsize:int = 4
 basetime:int = 'I64_MIN'
 font:str = "Sans"
 expansion:DRAWTEXT_EXPANSION = 'normal'
 timecode:str = None
 tc24hmax:bool = False
 timecode_rate:float|str = '0/1'
 r:float|str = '0/1'
 rate:float|str = '0/1'
 reload:int = 0
 alpha:str = "1"
 fix_bounds:bool = False
 start_number:int = 0
 text_source:str = None
 ft_load_flags:DRAWTEXT_FT_LOAD_FLAGS = '0' 
 ...


EDGEDETECT_MODE = Literal['wires', 'colormix', 'canny']
EDGEDETECT_PLANES = Literal['y', 'u', 'v', 'r', 'g', 'b']

@dataclass
class edgedetect(): # edgedetect
 high:float = '0.196078'
 low:float = '0.0784314'
 mode:EDGEDETECT_MODE = 'wires'
 planes:EDGEDETECT_PLANES = 'y+u+v+r+g+b' 
 ...




@dataclass
class elbg(): # elbg
 codebook_length:int = 256
 l:int = 256
 nb_steps:int = 1
 n:int = 1
 seed:int = -1
 s:int = -1
 pal8:bool = False
 use_alpha:bool = False 
 ...


ENTROPY_MODE = Literal['normal', 'diff']

@dataclass
class entropy(): # entropy
 mode:ENTROPY_MODE = 'normal' 
 ...




@dataclass
class epx(): # epx
 n:int = 3 
 ...


EQ_EVAL = Literal['init', 'frame']

@dataclass
class eq(): # eq
 contrast:str = "1.0"
 brightness:str = "0.0"
 saturation:str = "1.0"
 gamma:str = "1.0"
 gamma_r:str = "1.0"
 gamma_g:str = "1.0"
 gamma_b:str = "1.0"
 gamma_weight:str = "1.0"
 eval:EQ_EVAL = 'init' 
 ...


ESTDIF_MODE = Literal['frame', 'field']
ESTDIF_PARITY = Literal['tff', 'bff', 'auto']
ESTDIF_DEINT = Literal['all', 'interlaced']
ESTDIF_INTERP = Literal['2p', '4p', '6p']

@dataclass
class estdif(): # estdif
 mode:ESTDIF_MODE = 'field'
 parity:ESTDIF_PARITY = 'auto'
 deint:ESTDIF_DEINT = 'all'
 rslope:int = 1
 redge:int = 2
 ecost:float = '1'
 mcost:float = '0.5'
 dcost:float = '0.5'
 interp:ESTDIF_INTERP = '4p' 
 ...




@dataclass
class exposure(): # exposure
 exposure:float = '0'
 black:float = '0' 
 ...


EXTRACTPLANES_PLANES = Literal['y', 'u', 'v', 'r', 'g', 'b', 'a']

@dataclass
class extractplanes(): # extractplanes
 planes:EXTRACTPLANES_PLANES = 'r' 
 ...


FADE_TYPE = Literal['in', 'out']

@dataclass
class fade(): # fade
 type:FADE_TYPE = 'in'
 t:FADE_TYPE = 'in'
 start_frame:int = 0
 s:int = 0
 nb_frames:int = 25
 n:int = 25
 alpha:bool = False
 start_time:str = '0'
 st:str = '0'
 duration:str = '0'
 d:str = '0'
 color:COLORS = "black"
 c:COLORS = "black" 
 ...




@dataclass
class feedback(): # feedback
 x:int = 0
 y:int = 0
 w:int = 0
 h:int = 0 
 ...


FFTDNOIZ_METHOD = Literal['wiener', 'hard']
FFTDNOIZ_WINDOW = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']

@dataclass
class fftdnoiz(): # fftdnoiz
 sigma:float = '1'
 amount:float = '1'
 block:int = 32
 overlap:float = '0.5'
 method:FFTDNOIZ_METHOD = 'wiener'
 prev:int = 0
 next:int = 0
 planes:int = 7
 window:FFTDNOIZ_WINDOW = 'hann' 
 ...


FFTFILT_EVAL = Literal['init', 'frame']

@dataclass
class fftfilt(): # fftfilt
 dc_Y:int = 0
 dc_U:int = 0
 dc_V:int = 0
 weight_Y:str = "1"
 weight_U:str = None
 weight_V:str = None
 eval:FFTFILT_EVAL = 'init' 
 ...


FIELD_TYPE = Literal['top', 'bottom']

@dataclass
class field(): # field
 type:FIELD_TYPE = 'top' 
 ...


FIELDHINT_MODE = Literal['absolute', 'relative', 'pattern']

@dataclass
class fieldhint(): # fieldhint
 hint:str = None
 mode:FIELDHINT_MODE = 'absolute' 
 ...


FIELDMATCH_ORDER = Literal['auto', 'bff', 'tff']
FIELDMATCH_MODE = Literal['pc', 'pc_n', 'pc_u', 'pc_n_ub', 'pcn', 'pcn_ub']
FIELDMATCH_FIELD = Literal['auto', 'bottom', 'top']
FIELDMATCH_COMBMATCH = Literal['none', 'sc', 'full']
FIELDMATCH_COMBDBG = Literal['none', 'pcn', 'pcnub']

@dataclass
class fieldmatch(): # fieldmatch
 order:FIELDMATCH_ORDER = 'auto'
 mode:FIELDMATCH_MODE = 'pc_n'
 ppsrc:bool = False
 field:FIELDMATCH_FIELD = 'auto'
 mchroma:bool = True
 y0:int = 0
 y1:int = 0
 scthresh:float = '12'
 combmatch:FIELDMATCH_COMBMATCH = 'sc'
 combdbg:FIELDMATCH_COMBDBG = 'none'
 cthresh:int = 9
 chroma:bool = False
 blockx:int = 16
 blocky:int = 16
 combpel:int = 80 
 ...


FIELDORDER_ORDER = Literal['bff', 'tff']

@dataclass
class fieldorder(): # fieldorder
 order:FIELDORDER_ORDER = 'tff' 
 ...


FILLBORDERS_MODE = Literal['smear', 'mirror', 'fixed', 'reflect', 'wrap', 'fade', 'margins']

@dataclass
class fillborders(): # fillborders
 left:int = 0
 right:int = 0
 top:int = 0
 bottom:int = 0
 mode:FILLBORDERS_MODE = 'smear'
 color:COLORS = "black" 
 ...




@dataclass
class find_rect(): # find_rect
 object:str = None
 threshold:float = '0.5'
 mipmaps:int = 3
 xmin:int = 0
 ymin:int = 0
 xmax:int = 0
 ymax:int = 0
 discard:bool = False 
 ...




@dataclass
class floodfill(): # floodfill
 x:int = 0
 y:int = 0
 s0:int = 0
 s1:int = 0
 s2:int = 0
 s3:int = 0
 d0:int = 0
 d1:int = 0
 d2:int = 0
 d3:int = 0 
 ...




@dataclass
class _no_format(): # (no)format
 pix_fmts:str = None 
 ...


FPS_ROUND = Literal['zero', 'inf', 'down', 'up', 'near']
FPS_EOF_ACTION = Literal['round', 'pass']

@dataclass
class fps(): # fps
 fps:str = "25"
 start_time:float = 'DBL_MAX'
 round:FPS_ROUND = 'near'
 eof_action:FPS_EOF_ACTION = 'round' 
 ...


FRAMEPACK_FORMAT = Literal['sbs', 'tab', 'frameseq', 'lines', 'columns']

@dataclass
class framepack(): # framepack
 format:FRAMEPACK_FORMAT = 'sbs' 
 ...


FRAMERATE_FLAGS = Literal['scene_change_detect', 'scd']

@dataclass
class framerate(): # framerate
 fps:VIDEO_RATES = "50"
 interp_start:int = 15
 interp_end:int = 240
 scene:float = '8.2'
 flags:FRAMERATE_FLAGS = 'scene_change_detect+scd' 
 ...




@dataclass
class framestep(): # framestep
 step:int = 1 
 ...




@dataclass
class freezedetect(): # freezedetect
 n:float = '0.001'
 noise:float = '0.001'
 d:str = '2'
 duration:str = '2' 
 ...




@dataclass
class freezeframes(): # freezeframes
 first:int = 0
 last:int = 0
 replace:int = 0 
 ...




@dataclass
class frei0r(): # frei0r
 filter_name:str = None
 filter_params:str = None 
 ...




@dataclass
class fspp(): # fspp
 quality:int = 4
 qp:int = 0
 strength:int = 0
 use_bframe_qp:bool = False 
 ...




@dataclass
class gblur(): # gblur
 sigma:float = '0.5'
 steps:int = 1
 planes:int = 15
 sigmaV:float = '-1' 
 ...


GEQ_INTERPOLATION = Literal['nearest', 'n', 'bilinear', 'b']

@dataclass
class geq(): # geq
 lum_expr:str = None
 lum:str = None
 cb_expr:str = None
 cb:str = None
 cr_expr:str = None
 cr:str = None
 alpha_expr:str = None
 a:str = None
 red_expr:str = None
 r:str = None
 green_expr:str = None
 g:str = None
 blue_expr:str = None
 b:str = None
 interpolation:GEQ_INTERPOLATION = 'bilinear'
 i:GEQ_INTERPOLATION = 'bilinear' 
 ...




@dataclass
class gradfun(): # gradfun
 strength:float = '1.2'
 radius:int = 16 
 ...


_A_GRAPHMONITOR_MODE = Literal['full', 'compact']
_A_GRAPHMONITOR_FLAGS = Literal['queue', 'frame_count_in', 'frame_count_out', 'frame_count_delta', 'pts', 'pts_delta', 'time', 'time_delta', 'timebase', 'format', 'size', 'rate', 'eof', 'sample_count_in', 'sample_count_out', 'sample_count_delta']

@dataclass
class _a_graphmonitor(): # (a)graphmonitor
 size:IMAGE_SIZES = "hd720"
 s:IMAGE_SIZES = "hd720"
 opacity:float = '0.9'
 o:float = '0.9'
 mode:_A_GRAPHMONITOR_MODE = 'full'
 m:_A_GRAPHMONITOR_MODE = 'full'
 flags:_A_GRAPHMONITOR_FLAGS = 'queue'
 f:_A_GRAPHMONITOR_FLAGS = 'queue'
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25" 
 ...




@dataclass
class grayworld(): # grayworld 
 ...




@dataclass
class greyedge(): # greyedge
 difford:int = 1
 minknorm:int = 1
 sigma:float = '1' 
 ...


GUIDED_MODE = Literal['basic', 'fast']
GUIDED_GUIDANCE = Literal['off', 'on']

@dataclass
class guided(): # guided
 radius:int = 3
 eps:float = '0.01'
 mode:GUIDED_MODE = 'basic'
 sub:int = 4
 guidance:GUIDED_GUIDANCE = 'off'
 planes:int = 1 
 ...


HALDCLUT_CLUT = Literal['first', 'all']
HALDCLUT_INTERP = Literal['nearest', 'trilinear', 'tetrahedral', 'pyramid', 'prism']

@dataclass
class haldclut(): # haldclut
 clut:HALDCLUT_CLUT = 'all'
 interp:HALDCLUT_INTERP = 'tetrahedral' 
 ...




@dataclass
class hflip(): # hflip 
 ...


HISTEQ_ANTIBANDING = Literal['none', 'weak', 'strong']

@dataclass
class histeq(): # histeq
 strength:float = '0.2'
 intensity:float = '0.21'
 antibanding:HISTEQ_ANTIBANDING = 'none' 
 ...


HISTOGRAM_DISPLAY_MODE = Literal['overlay', 'parade', 'stack']
HISTOGRAM_LEVELS_MODE = Literal['linear', 'logarithmic']
HISTOGRAM_COLORS_MODE = Literal['whiteonblack', 'blackonwhite', 'whiteongray', 'blackongray', 'coloronblack', 'coloronwhite', 'colorongray', 'blackoncolor', 'whiteoncolor', 'grayoncolor']

@dataclass
class histogram(): # histogram
 level_height:int = 200
 scale_height:int = 12
 display_mode:HISTOGRAM_DISPLAY_MODE = 'stack'
 d:HISTOGRAM_DISPLAY_MODE = 'stack'
 levels_mode:HISTOGRAM_LEVELS_MODE = 'linear'
 m:HISTOGRAM_LEVELS_MODE = 'linear'
 components:int = 7
 c:int = 7
 fgopacity:float = '0.7'
 f:float = '0.7'
 bgopacity:float = '0.5'
 b:float = '0.5'
 colors_mode:HISTOGRAM_COLORS_MODE = 'whiteonblack'
 l:HISTOGRAM_COLORS_MODE = 'whiteonblack' 
 ...




@dataclass
class hqdn3d(): # hqdn3d
 luma_spatial:float = '0'
 chroma_spatial:float = '0'
 luma_tmp:float = '0'
 chroma_tmp:float = '0' 
 ...




@dataclass
class hqx(): # hqx
 n:int = 3 
 ...




@dataclass
class _h_v_stack(): # (h|v)stack
 inputs:int = 2
 shortest:bool = False 
 ...




@dataclass
class hsvhold(): # hsvhold
 hue:float = '0'
 sat:float = '0'
 val:float = '0'
 similarity:float = '0.01'
 blend:float = '0' 
 ...




@dataclass
class hsvkey(): # hsvkey
 hue:float = '0'
 sat:float = '0'
 val:float = '0'
 similarity:float = '0.01'
 blend:float = '0' 
 ...




@dataclass
class hue(): # hue
 h:str = None
 s:str = "1"
 H:str = None
 b:str = "0" 
 ...


HUESATURATION_COLORS = Literal['r', 'y', 'g', 'c', 'b', 'm', 'a']

@dataclass
class huesaturation(): # huesaturation
 hue:float = '0'
 saturation:float = '0'
 intensity:float = '0'
 colors:HUESATURATION_COLORS = 'r+y+g+c+b+m+a'
 strength:float = '1'
 rw:float = '0.333'
 gw:float = '0.334'
 bw:float = '0.333'
 lightness:bool = False 
 ...


HWMAP_MODE = Literal['read', 'write', 'overwrite', 'direct']

@dataclass
class hwmap(): # hwmap
 mode:HWMAP_MODE = 'read+write'
 derive_device:str = None
 reverse:int = 0 
 ...




@dataclass
class hwupload(): # hwupload
 derive_device:str = None 
 ...




@dataclass
class hysteresis(): # hysteresis
 planes:int = 15
 threshold:int = 0 
 ...




@dataclass
class identity(): # identity 
 ...




@dataclass
class idet(): # idet
 intl_thres:float = '1.04'
 prog_thres:float = '1.5'
 rep_thres:float = '3'
 half_life:float = '0'
 analyze_interlaced_flag:int = 0 
 ...


IL_LUMA_MODE = Literal['none', 'interleave', 'i', 'deinterleave', 'd']

@dataclass
class il(): # il
 luma_mode:IL_LUMA_MODE = 'none'
 l:IL_LUMA_MODE = 'none'
 chroma_mode:IL_LUMA_MODE = 'none'
 c:IL_LUMA_MODE = 'none'
 alpha_mode:IL_LUMA_MODE = 'none'
 a:IL_LUMA_MODE = 'none'
 luma_swap:bool = False
 ls:bool = False
 chroma_swap:bool = False
 cs:bool = False
 alpha_swap:bool = False
 _as:bool = dataclasses_field(default=False, metadata='as') 
 ...


INTERLACE_SCAN = Literal['tff', 'bff']
INTERLACE_LOWPASS = Literal['off', 'linear', 'complex']

@dataclass
class interlace(): # interlace
 scan:INTERLACE_SCAN = 'tff'
 lowpass:INTERLACE_LOWPASS = 'linear' 
 ...


INTERLEAVE_DURATION = Literal['longest', 'shortest', 'first']

@dataclass
class interleave(): # interleave
 nb_inputs:int = 2
 n:int = 2
 duration:INTERLEAVE_DURATION = 'longest' 
 ...




@dataclass
class kerndeint(): # kerndeint
 thresh:int = 10
 map:bool = False
 order:bool = False
 sharp:bool = False
 twoway:bool = False 
 ...




@dataclass
class kirsch_prewitt_roberts_scharr_sobel(): # kirsch/prewitt/roberts/scharr/sobel
 planes:int = 15
 scale:float = '1'
 delta:float = '0' 
 ...




@dataclass
class lagfun(): # lagfun
 decay:float = '0.95'
 planes:str = 'F' 
 ...


LENSCORRECTION_I = Literal['nearest', 'bilinear']

@dataclass
class lenscorrection(): # lenscorrection
 cx:float = '0.5'
 cy:float = '0.5'
 k1:float = '0'
 k2:float = '0'
 i:LENSCORRECTION_I = 'nearest'
 fc:COLORS = "black@0" 
 ...




@dataclass
class libvmaf(): # libvmaf
 model_path:str = None
 log_path:str = None
 log_fmt:str = "xml"
 enable_transform:bool = False
 phone_model:bool = False
 psnr:bool = False
 ssim:bool = False
 ms_ssim:bool = False
 pool:str = None
 n_threads:int = 0
 n_subsample:int = 1
 enable_conf_interval:bool = False
 model:str = "version=vmaf_v0.6.1"
 feature:str = None 
 ...




@dataclass
class limitdiff(): # limitdiff
 threshold:float = '0.00392157'
 elasticity:float = '2'
 reference:bool = False
 planes:int = 15 
 ...




@dataclass
class limiter(): # limiter
 min:int = 0
 max:int = 65535
 planes:int = 15 
 ...




@dataclass
class loop(): # loop
 loop:int = 0
 size:int = 0
 start:int = 0 
 ...




@dataclass
class lumakey(): # lumakey
 threshold:float = '0'
 tolerance:float = '0.01'
 softness:float = '0' 
 ...




@dataclass
class lut_lutyuv_lutrgb(): # lut/lutyuv/lutrgb
 c0:str = "clipval"
 c1:str = "clipval"
 c2:str = "clipval"
 c3:str = "clipval"
 y:str = "clipval"
 u:str = "clipval"
 v:str = "clipval"
 r:str = "clipval"
 g:str = "clipval"
 b:str = "clipval"
 a:str = "clipval" 
 ...


LUT1D_INTERP = Literal['nearest', 'linear', 'cosine', 'cubic', 'spline']

@dataclass
class lut1d(): # lut1d
 file:str = None
 interp:LUT1D_INTERP = 'linear' 
 ...




@dataclass
class lut2(): # lut2
 c0:str = "x"
 c1:str = "x"
 c2:str = "x"
 c3:str = "x"
 d:int = 0 
 ...


LUT3D_CLUT = Literal['first', 'all']
LUT3D_INTERP = Literal['nearest', 'trilinear', 'tetrahedral', 'pyramid', 'prism']

@dataclass
class lut3d(): # lut3d
 file:str = None
 clut:LUT3D_CLUT = 'all'
 interp:LUT3D_INTERP = 'tetrahedral' 
 ...




@dataclass
class maskedclamp(): # maskedclamp
 undershoot:int = 0
 overshoot:int = 0
 planes:int = 15 
 ...




@dataclass
class masked_min_max_(): # masked(min|max)
 planes:int = 15 
 ...




@dataclass
class maskedmerge(): # maskedmerge
 planes:int = 15 
 ...


MASKEDTHRESHOLD_MODE = Literal['abs', 'diff']

@dataclass
class maskedthreshold(): # maskedthreshold
 threshold:int = 1
 planes:int = 15
 mode:MASKEDTHRESHOLD_MODE = 'abs' 
 ...




@dataclass
class maskfun(): # maskfun
 low:int = 10
 high:int = 10
 planes:int = 15
 fill:int = 0
 sum:int = 10 
 ...




@dataclass
class median(): # median
 radius:int = 1
 planes:int = 15
 radiusV:int = 0
 percentile:float = '0.5' 
 ...




@dataclass
class mergeplanes(): # mergeplanes
 mapping:int = -1
 format:PIXEL_FORMATS = 'yuva444p'
 map0s:int = 0
 map0p:int = 0
 map1s:int = 0
 map1p:int = 0
 map2s:int = 0
 map2p:int = 0
 map3s:int = 0
 map3p:int = 0 
 ...


MESTIMATE_METHOD = Literal['esa', 'tss', 'tdls', 'ntss', 'fss', 'ds', 'hexbs', 'epzs', 'umh']

@dataclass
class mestimate(): # mestimate
 method:MESTIMATE_METHOD = 'esa'
 mb_size:int = 16
 search_param:int = 7 
 ...


METADATA_MODE = Literal['select', 'add', 'modify', 'delete', 'print']
METADATA_FUNCTION = Literal['same_str', 'starts_with', 'less', 'equal', 'greater', 'expr', 'ends_with']

@dataclass
class metadata(): # metadata
 mode:METADATA_MODE = 'select'
 key:str = None
 value:str = None
 function:METADATA_FUNCTION = 'same_str'
 expr:str = None
 file:str = None
 direct:bool = False 
 ...




@dataclass
class midequalizer(): # midequalizer
 planes:int = 15 
 ...


MINTERPOLATE_MI_MODE = Literal['dup', 'blend', 'mci']
MINTERPOLATE_MC_MODE = Literal['obmc', 'aobmc']
MINTERPOLATE_ME_MODE = Literal['bidir', 'bilat']
MINTERPOLATE_ME = Literal['esa', 'tss', 'tdls', 'ntss', 'fss', 'ds', 'hexbs', 'epzs', 'umh']
MINTERPOLATE_SCD = Literal['none', 'fdiff']

@dataclass
class minterpolate(): # minterpolate
 fps:VIDEO_RATES = "60"
 mi_mode:MINTERPOLATE_MI_MODE = 'mci'
 mc_mode:MINTERPOLATE_MC_MODE = 'obmc'
 me_mode:MINTERPOLATE_ME_MODE = 'bilat'
 me:MINTERPOLATE_ME = 'epzs'
 mb_size:int = 16
 search_param:int = 32
 vsbmc:int = 0
 scd:MINTERPOLATE_SCD = 'fdiff'
 scd_threshold:float = '10' 
 ...


MIX_DURATION = Literal['longest', 'shortest', 'first']

@dataclass
class mix(): # mix
 inputs:int = 2
 weights:str = "1 1"
 scale:float = '0'
 planes:str = 'F'
 duration:MIX_DURATION = 'longest' 
 ...




@dataclass
class monochrome(): # monochrome
 cb:float = '0'
 cr:float = '0'
 size:float = '1'
 high:float = '0' 
 ...


MORPHO_MODE = Literal['erode', 'dilate', 'open', 'close', 'gradient', 'tophat', 'blackhat']
MORPHO_STRUCTURE = Literal['first', 'all']

@dataclass
class morpho(): # morpho
 mode:MORPHO_MODE = 'erode'
 planes:int = 7
 structure:MORPHO_STRUCTURE = 'all' 
 ...




@dataclass
class mpdecimate(): # mpdecimate
 max:int = 0
 hi:int = 768
 lo:int = 320
 frac:float = '0.33' 
 ...




@dataclass
class msad(): # msad 
 ...




@dataclass
class multiply(): # multiply
 scale:float = '1'
 offset:float = '0.5'
 planes:str = 'F' 
 ...


NEGATE_COMPONENTS = Literal['y', 'u', 'v', 'r', 'g', 'b', 'a']

@dataclass
class negate(): # negate
 components:NEGATE_COMPONENTS = 'y+u+v+r+g+b'
 negate_alpha:bool = False 
 ...




@dataclass
class nlmeans(): # nlmeans
 s:float = '1'
 p:int = 7
 pc:int = 0
 r:int = 15
 rc:int = 0 
 ...


NNEDI_DEINT = Literal['all', 'interlaced']
NNEDI_FIELD = Literal['af', 'a', 't', 'b', 'tf', 'bf']
NNEDI_NSIZE = Literal['s8x6', 's16x6', 's32x6', 's48x6', 's8x4', 's16x4', 's32x4']
NNEDI_NNS = Literal['n16', 'n32', 'n64', 'n128', 'n256']
NNEDI_QUAL = Literal['fast', 'slow']
NNEDI_ETYPE = Literal['a', 'abs', 's', 'mse']
NNEDI_PSCRN = Literal['none', 'original', 'new', 'new2', 'new3']

@dataclass
class nnedi(): # nnedi
 weights:str = "nnedi3_weights.bin"
 deint:NNEDI_DEINT = 'all'
 field:NNEDI_FIELD = 'a'
 planes:int = 7
 nsize:NNEDI_NSIZE = 's32x4'
 nns:NNEDI_NNS = 'n32'
 qual:NNEDI_QUAL = 'fast'
 etype:NNEDI_ETYPE = 'a'
 pscrn:NNEDI_PSCRN = 'new' 
 ...


NOISE_ALL_FLAGS = Literal['a', 'p', 't', 'u']

@dataclass
class noise(): # noise
 all_seed:int = -1
 all_strength:int = 0
 alls:int = 0
 all_flags:NOISE_ALL_FLAGS = '0'
 allf:NOISE_ALL_FLAGS = '0'
 c0_seed:int = -1
 c0_strength:int = 0
 c0s:int = 0
 c0_flags:NOISE_ALL_FLAGS = '0'
 c0f:NOISE_ALL_FLAGS = '0'
 c1_seed:int = -1
 c1_strength:int = 0
 c1s:int = 0
 c1_flags:NOISE_ALL_FLAGS = '0'
 c1f:NOISE_ALL_FLAGS = '0'
 c2_seed:int = -1
 c2_strength:int = 0
 c2s:int = 0
 c2_flags:NOISE_ALL_FLAGS = '0'
 c2f:NOISE_ALL_FLAGS = '0'
 c3_seed:int = -1
 c3_strength:int = 0
 c3s:int = 0
 c3_flags:NOISE_ALL_FLAGS = '0'
 c3f:NOISE_ALL_FLAGS = '0' 
 ...




@dataclass
class normalize(): # normalize
 blackpt:COLORS = "black"
 whitept:COLORS = "white"
 smoothing:int = 0
 independence:float = '1'
 strength:float = '1' 
 ...




@dataclass
class ocr(): # ocr
 datapath:str = None
 language:str = "eng"
 whitelist:str = None
 blacklist:str = "" 
 ...




@dataclass
class oscilloscope(): # oscilloscope
 x:float = '0.5'
 y:float = '0.5'
 s:float = '0.8'
 t:float = '0.5'
 o:float = '0.8'
 tx:float = '0.5'
 ty:float = '0.9'
 tw:float = '0.8'
 th:float = '0.3'
 c:int = 7
 g:bool = True
 st:bool = True
 sc:bool = True 
 ...


OVERLAY_EOF_ACTION = Literal['repeat', 'endall', 'pass']
OVERLAY_EVAL = Literal['init', 'frame']
OVERLAY_FORMAT = Literal['yuv420', 'yuv420p10', 'yuv422', 'yuv422p10', 'yuv444', 'rgb', 'gbrp', 'auto']
OVERLAY_ALPHA = Literal['straight', 'premultiplied']

@dataclass
class overlay(): # overlay
 x:str = "0"
 y:str = "0"
 eof_action:OVERLAY_EOF_ACTION = 'repeat'
 eval:OVERLAY_EVAL = 'frame'
 shortest:bool = False
 format:OVERLAY_FORMAT = 'yuv420'
 repeatlast:bool = True
 alpha:OVERLAY_ALPHA = 'straight' 
 ...




@dataclass
class owdenoise(): # owdenoise
 depth:int = 8
 luma_strength:float = '1'
 ls:float = '1'
 chroma_strength:float = '1'
 cs:float = '1' 
 ...


PAD_EVAL = Literal['init', 'frame']

@dataclass
class pad(): # pad
 width:str = "iw"
 w:str = "iw"
 height:str = "ih"
 h:str = "ih"
 x:str = "0"
 y:str = "0"
 color:COLORS = "black"
 eval:PAD_EVAL = 'init'
 aspect:float|str = '0/1' 
 ...


PALETTEGEN_STATS_MODE = Literal['full', 'diff', 'single']

@dataclass
class palettegen(): # palettegen
 max_colors:int = 256
 reserve_transparent:bool = True
 transparency_color:COLORS = "lime"
 stats_mode:PALETTEGEN_STATS_MODE = 'full' 
 ...


PALETTEUSE_DITHER = Literal['bayer', 'heckbert', 'floyd_steinberg', 'sierra2', 'sierra2_4a', 'sierra3', 'burkes', 'atkinson']
PALETTEUSE_DIFF_MODE = Literal['rectangle']

@dataclass
class paletteuse(): # paletteuse
 dither:PALETTEUSE_DITHER = 'sierra2_4a'
 bayer_scale:int = 2
 diff_mode:PALETTEUSE_DIFF_MODE = '0'
 new:bool = False
 alpha_threshold:int = 128
 debug_kdtree:str = None 
 ...


PERSPECTIVE_INTERPOLATION = Literal['linear', 'cubic']
PERSPECTIVE_SENSE = Literal['source', 'destination']
PERSPECTIVE_EVAL = Literal['init', 'frame']

@dataclass
class perspective(): # perspective
 x0:str = "0"
 y0:str = "0"
 x1:str = "W"
 y1:str = "0"
 x2:str = "0"
 y2:str = "H"
 x3:str = "W"
 y3:str = "H"
 interpolation:PERSPECTIVE_INTERPOLATION = 'linear'
 sense:PERSPECTIVE_SENSE = 'source'
 eval:PERSPECTIVE_EVAL = 'init' 
 ...


PHASE_MODE = Literal['p', 't', 'b', 'T', 'B', 'u', 'U', 'a', 'A']

@dataclass
class phase(): # phase
 mode:PHASE_MODE = 'A' 
 ...




@dataclass
class photosensitivity(): # photosensitivity
 frames:int = 30
 f:int = 30
 threshold:float = '1'
 t:float = '1'
 skip:int = 1
 bypass:bool = False 
 ...


PIXELIZE_MODE = Literal['avg', 'min', 'max']

@dataclass
class pixelize(): # pixelize
 width:int = 16
 w:int = 16
 height:int = 16
 h:int = 16
 mode:PIXELIZE_MODE = 'avg'
 m:PIXELIZE_MODE = 'avg'
 planes:str = 'F'
 p:str = 'F' 
 ...




@dataclass
class pixscope(): # pixscope
 x:float = '0.5'
 y:float = '0.5'
 w:int = 7
 h:int = 7
 o:float = '0.5'
 wx:float = '-1'
 wy:float = '-1' 
 ...




@dataclass
class pp(): # pp
 subfilters:str = "de" 
 ...


PP7_MODE = Literal['hard', 'soft', 'medium']

@dataclass
class pp7(): # pp7
 qp:int = 0
 mode:PP7_MODE = 'medium' 
 ...




@dataclass
class _un_premultiply(): # (un)premultiply
 planes:int = 15
 inplace:bool = False 
 ...


PSEUDOCOLOR_PRESET = Literal['none', 'magma', 'inferno', 'plasma', 'viridis', 'turbo', 'cividis', 'range1', 'range2', 'shadows', 'highlights', 'solar', 'nominal', 'preferred', 'total', 'spectral']

@dataclass
class pseudocolor(): # pseudocolor
 c0:str = "val"
 c1:str = "val"
 c2:str = "val"
 c3:str = "val"
 index:int = 0
 i:int = 0
 preset:PSEUDOCOLOR_PRESET = 'none'
 p:PSEUDOCOLOR_PRESET = 'none'
 opacity:float = '1' 
 ...




@dataclass
class psnr(): # psnr
 stats_file:str = None
 f:str = None
 stats_version:int = 1
 output_max:bool = False 
 ...


PULLUP_MP = Literal['y', 'u', 'v']

@dataclass
class pullup(): # pullup
 jl:int = 1
 jr:int = 1
 jt:int = 4
 jb:int = 4
 sb:bool = False
 mp:PULLUP_MP = 'y' 
 ...




@dataclass
class qp(): # qp
 qp:str = None 
 ...




@dataclass
class random(): # random
 frames:int = 30
 seed:int = -1 
 ...




@dataclass
class readeia608(): # readeia608
 scan_min:int = 0
 scan_max:int = 29
 spw:float = '0.27'
 chp:bool = False
 lp:bool = True 
 ...




@dataclass
class readvitc(): # readvitc
 scan_max:int = 45
 thr_b:float = '0.2'
 thr_w:float = '0.6' 
 ...


REMAP_FORMAT = Literal['color', 'gray']

@dataclass
class remap(): # remap
 format:REMAP_FORMAT = 'color'
 fill:COLORS = "black" 
 ...




@dataclass
class removegrain(): # removegrain
 m0:int = 0
 m1:int = 0
 m2:int = 0
 m3:int = 0 
 ...




@dataclass
class removelogo(): # removelogo
 filename:str = None
 f:str = None 
 ...


RGBASHIFT_EDGE = Literal['smear', 'wrap']

@dataclass
class rgbashift(): # rgbashift
 rh:int = 0
 rv:int = 0
 gh:int = 0
 gv:int = 0
 bh:int = 0
 bv:int = 0
 ah:int = 0
 av:int = 0
 edge:RGBASHIFT_EDGE = 'smear' 
 ...




@dataclass
class rotate(): # rotate
 angle:str = "0"
 a:str = "0"
 out_w:str = "iw"
 ow:str = "iw"
 out_h:str = "ih"
 oh:str = "ih"
 fillcolor:str = "black"
 c:str = "black"
 bilinear:bool = True 
 ...




@dataclass
class sab(): # sab
 luma_radius:float = '1'
 lr:float = '1'
 luma_pre_filter_radius:float = '1'
 lpfr:float = '1'
 luma_strength:float = '1'
 ls:float = '1'
 chroma_radius:float = '-0.9'
 cr:float = '-0.9'
 chroma_pre_filter_radius:float = '-0.9'
 cpfr:float = '-0.9'
 chroma_strength:float = '-0.9'
 cs:float = '-0.9' 
 ...


SCALE_2REF__IN_COLOR_MATRIX = Literal['auto', 'bt601', 'bt470', 'smpte170m', 'bt709', 'fcc', 'smpte240m', 'bt2020']
SCALE_2REF__IN_RANGE = Literal['auto', 'unknown', 'full', 'limited', 'jpeg', 'mpeg', 'tv', 'pc']
SCALE_2REF__FORCE_ORIGINAL_ASPECT_RATIO = Literal['disable', 'decrease', 'increase']
SCALE_2REF__EVAL = Literal['init', 'frame']

@dataclass
class scale_2ref_(): # scale(2ref)
 w:str = None
 width:str = None
 h:str = None
 height:str = None
 flags:str = ""
 interl:bool = False
 in_color_matrix:SCALE_2REF__IN_COLOR_MATRIX = "auto"
 out_color_matrix:SCALE_2REF__IN_COLOR_MATRIX = 'None'
 in_range:SCALE_2REF__IN_RANGE = 'auto'
 out_range:SCALE_2REF__IN_RANGE = 'auto'
 in_v_chr_pos:int = -513
 in_h_chr_pos:int = -513
 out_v_chr_pos:int = -513
 out_h_chr_pos:int = -513
 force_original_aspect_ratio:SCALE_2REF__FORCE_ORIGINAL_ASPECT_RATIO = 'disable'
 force_divisible_by:int = 1
 param0:float = 'DBL_MAX'
 param1:float = 'DBL_MAX'
 eval:SCALE_2REF__EVAL = 'init' 
 ...




@dataclass
class scdet(): # scdet
 threshold:float = '10'
 t:float = '10'
 sc_pass:bool = False
 s:bool = False 
 ...




@dataclass
class scroll(): # scroll
 horizontal:float = '0'
 h:float = '0'
 vertical:float = '0'
 v:float = '0'
 hpos:float = '0'
 vpos:float = '0' 
 ...




@dataclass
class segment(): # segment
 timestamps:str = None
 frames:str = None 
 ...




@dataclass
class select(): # select
 expr:str = "1"
 e:str = "1"
 outputs:int = 1
 n:int = 1 
 ...


SELECTIVECOLOR_CORRECTION_METHOD = Literal['absolute', 'relative']

@dataclass
class selectivecolor(): # selectivecolor
 correction_method:SELECTIVECOLOR_CORRECTION_METHOD = 'absolute'
 reds:str = None
 yellows:str = None
 greens:str = None
 cyans:str = None
 blues:str = None
 magentas:str = None
 whites:str = None
 neutrals:str = None
 blacks:str = None
 psfile:str = None 
 ...




@dataclass
class setdar(): # setdar
 dar:str = "0"
 ratio:str = "0"
 r:str = "0"
 max:int = 100 
 ...


SETFIELD_MODE = Literal['auto', 'bff', 'tff', 'prog']

@dataclass
class setfield(): # setfield
 mode:SETFIELD_MODE = 'auto' 
 ...


SETPARAMS_FIELD_MODE = Literal['auto', 'bff', 'tff', 'prog']
SETPARAMS_RANGE = Literal['auto', 'unspecified', 'unknown', 'limited', 'tv', 'mpeg', 'full', 'pc', 'jpeg']
SETPARAMS_COLOR_PRIMARIES = Literal['auto', 'bt709', 'unknown', 'bt470m', 'bt470bg', 'smpte170m', 'smpte240m', 'film', 'bt2020', 'smpte428', 'smpte431', 'smpte432', 'jedec-p22', 'ebu3213']
SETPARAMS_COLOR_TRC = Literal['auto', 'bt709', 'unknown', 'bt470m', 'bt470bg', 'smpte170m', 'smpte240m', 'linear', 'log100', 'log316', 'iec61966-2-4', 'bt1361e', 'iec61966-2-1', 'bt2020-10', 'bt2020-12', 'smpte2084', 'smpte428', 'arib-std-b67']
SETPARAMS_COLORSPACE = Literal['auto', 'gbr', 'bt709', 'unknown', 'fcc', 'bt470bg', 'smpte170m', 'smpte240m', 'ycgco', 'bt2020nc', 'bt2020c', 'smpte2085', 'chroma-derived-nc', 'chroma-derived-c', 'ictcp']

@dataclass
class setparams(): # setparams
 field_mode:SETPARAMS_FIELD_MODE = 'auto'
 range:SETPARAMS_RANGE = 'auto'
 color_primaries:SETPARAMS_COLOR_PRIMARIES = 'auto'
 color_trc:SETPARAMS_COLOR_TRC = 'auto'
 colorspace:SETPARAMS_COLORSPACE = 'auto' 
 ...




@dataclass
class setpts(): # setpts
 expr:str = "PTS" 
 ...


SETRANGE_RANGE = Literal['auto', 'unspecified', 'unknown', 'limited', 'tv', 'mpeg', 'full', 'pc', 'jpeg']

@dataclass
class setrange(): # setrange
 range:SETRANGE_RANGE = 'auto' 
 ...




@dataclass
class setsar(): # setsar
 sar:str = "0"
 ratio:str = "0"
 r:str = "0"
 max:int = 100 
 ...




@dataclass
class settb(): # settb
 expr:str = "intb"
 tb:str = "intb" 
 ...


SHEAR_INTERP = Literal['nearest', 'bilinear']

@dataclass
class shear(): # shear
 shx:float = '0'
 shy:float = '0'
 fillcolor:str = "black"
 c:str = "black"
 interp:SHEAR_INTERP = 'bilinear' 
 ...




@dataclass
class showinfo(): # showinfo
 checksum:bool = True 
 ...




@dataclass
class showpalette(): # showpalette
 s:int = 30 
 ...




@dataclass
class shuffleframes(): # shuffleframes
 mapping:str = "0" 
 ...


SHUFFLEPIXELS_DIRECTION = Literal['forward', 'inverse']
SHUFFLEPIXELS_MODE = Literal['horizontal', 'vertical', 'block']

@dataclass
class shufflepixels(): # shufflepixels
 direction:SHUFFLEPIXELS_DIRECTION = 'forward'
 d:SHUFFLEPIXELS_DIRECTION = 'forward'
 mode:SHUFFLEPIXELS_MODE = 'horizontal'
 m:SHUFFLEPIXELS_MODE = 'horizontal'
 width:int = 10
 w:int = 10
 height:int = 10
 h:int = 10
 seed:int = -1
 s:int = -1 
 ...




@dataclass
class shuffleplanes(): # shuffleplanes
 map0:int = 0
 map1:int = 1
 map2:int = 2
 map3:int = 3 
 ...


SIDEDATA_MODE = Literal['select', 'delete']
SIDEDATA_TYPE = Literal['PANSCAN', 'A53_CC', 'STEREO3D', 'MATRIXENCODING', 'DOWNMIX_INFO', 'REPLAYGAIN', 'DISPLAYMATRIX', 'AFD', 'MOTION_VECTORS', 'SKIP_SAMPLES', 'AUDIO_SERVICE_TYPE', 'MASTERING_DISPLAY_METADATA', 'GOP_TIMECODE', 'SPHERICAL', 'CONTENT_LIGHT_LEVEL', 'ICC_PROFILE', 'S12M_TIMECOD', 'DYNAMIC_HDR_PLUS', 'REGIONS_OF_INTEREST', 'DETECTION_BOUNDING_BOXES', 'SEI_UNREGISTERED']

@dataclass
class sidedata(): # sidedata
 mode:SIDEDATA_MODE = 'select'
 type:SIDEDATA_TYPE = '-1' 
 ...


SIGNALSTATS_STAT = Literal['tout', 'vrep', 'brng']

@dataclass
class signalstats(): # signalstats
 stat:SIGNALSTATS_STAT = '0'
 out:SIGNALSTATS_STAT = '-1'
 c:COLORS = "yellow"
 color:COLORS = "yellow" 
 ...


SIGNATURE_DETECTMODE = Literal['off', 'full', 'fast']
SIGNATURE_FORMAT = Literal['binary', 'xml']

@dataclass
class signature(): # signature
 detectmode:SIGNATURE_DETECTMODE = 'off'
 nb_inputs:int = 1
 filename:str = ""
 format:SIGNATURE_FORMAT = 'binary'
 th_d:int = 9000
 th_dc:int = 60000
 th_xh:int = 116
 th_di:int = 0
 th_it:float = '0.5' 
 ...




@dataclass
class siti(): # siti
 print_summary:bool = False 
 ...




@dataclass
class smartblur(): # smartblur
 luma_radius:float = '1'
 lr:float = '1'
 luma_strength:float = '1'
 ls:float = '1'
 luma_threshold:int = 0
 lt:int = 0
 chroma_radius:float = '-0.9'
 cr:float = '-0.9'
 chroma_strength:float = '-2'
 cs:float = '-2'
 chroma_threshold:int = -31
 ct:int = -31 
 ...


SPP_MODE = Literal['hard', 'soft']

@dataclass
class spp(): # spp
 quality:int = 3
 qp:int = 0
 mode:SPP_MODE = 'hard'
 use_bframe_qp:bool = False 
 ...


AVDCT_DCT = Literal['auto', 'fastint', 'int', 'mmx', 'altivec', 'faan']
AVDCT_IDCT = Literal['auto', 'int', 'simple', 'simplemmx', 'arm', 'altivec', 'simplearm', 'simplearmv5te', 'simplearmv6', 'simpleneon', 'xvid', 'xvidmmx', 'faani', 'simpleauto']

@dataclass
class AVDCT(): # AVDCT
 dct:AVDCT_DCT = 'auto'
 idct:AVDCT_IDCT = 'auto' 
 ...


SR_DNN_BACKEND = Literal['native']

@dataclass
class sr(): # sr
 dnn_backend:SR_DNN_BACKEND = 'native'
 scale_factor:int = 2
 model:str = None
 input:str = "x"
 output:str = "y" 
 ...




@dataclass
class ssim(): # ssim
 stats_file:str = None
 f:str = None 
 ...


SSIM360_REF_PROJECTION = Literal['e', 'equirect', 'c3x2', 'c2x3', 'barrel', 'barrelsplit']
SSIM360_REF_STEREO = Literal['mono', 'tb', 'lr']

@dataclass
class ssim360(): # ssim360
 stats_file:str = None
 f:str = None
 compute_chroma:int = 1
 frame_skip_ratio:int = 0
 ref_projection:SSIM360_REF_PROJECTION = 'e'
 main_projection:SSIM360_REF_PROJECTION = '5'
 ref_stereo:SSIM360_REF_STEREO = 'mono'
 main_stereo:SSIM360_REF_STEREO = '3'
 ref_pad:float = '0'
 main_pad:float = '0'
 use_tape:int = 0
 heatmap_str:str = None
 default_heatmap_width:int = 32
 default_heatmap_height:int = 16 
 ...


STEREO3D__IN = Literal['ab2l', 'tb2l', 'ab2r', 'tb2r', 'abl', 'tbl', 'abr', 'tbr', 'al', 'ar', 'sbs2l', 'sbs2r', 'sbsl', 'sbsr', 'irl', 'irr', 'icl', 'icr']
STEREO3D_OUT = Literal['ab2l', 'tb2l', 'ab2r', 'tb2r', 'abl', 'tbl', 'abr', 'tbr', 'agmc', 'agmd', 'agmg', 'agmh', 'al', 'ar', 'arbg', 'arcc', 'arcd', 'arcg', 'arch', 'argg', 'aybc', 'aybd', 'aybg', 'aybh', 'irl', 'irr', 'ml', 'mr', 'sbs2l', 'sbs2r', 'sbsl', 'sbsr', 'chl', 'chr', 'icl', 'icr', 'hdmi']

@dataclass
class stereo3d(): # stereo3d
 _in:STEREO3D__IN = dataclasses_field(default='sbsl', metadata='in')
 out:STEREO3D_OUT = 'arcd' 
 ...




@dataclass
class subtitles(): # subtitles
 filename:str = None
 f:str = None
 original_size:IMAGE_SIZES = None
 fontsdir:str = None
 alpha:bool = False
 charenc:str = None
 stream_index:int = -1
 si:int = -1
 force_style:str = None 
 ...




@dataclass
class swaprect(): # swaprect
 w:str = "w/2"
 h:str = "h/2"
 x1:str = "w/2"
 y1:str = "h/2"
 x2:str = "0"
 y2:str = "0" 
 ...




@dataclass
class swapuv(): # swapuv 
 ...


TBLEND_C0_MODE = Literal['addition', 'addition128', 'grainmerge', 'and', 'average', 'burn', 'darken', 'difference', 'difference128', 'grainextract', 'divide', 'dodge', 'exclusion', 'extremity', 'freeze', 'glow', 'hardlight', 'hardmix', 'heat', 'lighten', 'linearlight', 'multiply', 'multiply128', 'negation', 'normal', 'or', 'overlay', 'phoenix', 'pinlight', 'reflect', 'screen', 'softlight', 'subtract', 'vividlight', 'xor', 'softdifference', 'geometric', 'harmonic', 'bleach', 'stain', 'interpolate', 'hardoverlay']

@dataclass
class tblend(): # tblend
 c0_mode:TBLEND_C0_MODE = 'normal'
 c1_mode:TBLEND_C0_MODE = 'normal'
 c2_mode:TBLEND_C0_MODE = 'normal'
 c3_mode:TBLEND_C0_MODE = 'normal'
 all_mode:TBLEND_C0_MODE = '-1'
 c0_expr:str = None
 c1_expr:str = None
 c2_expr:str = None
 c3_expr:str = None
 all_expr:str = None
 c0_opacity:float = '1'
 c1_opacity:float = '1'
 c2_opacity:float = '1'
 c3_opacity:float = '1'
 all_opacity:float = '1' 
 ...


TELECINE_FIRST_FIELD = Literal['top', 't', 'bottom', 'b']

@dataclass
class telecine(): # telecine
 first_field:TELECINE_FIRST_FIELD = 'top'
 pattern:str = "23" 
 ...


THISTOGRAM_DISPLAY_MODE = Literal['overlay', 'parade', 'stack']
THISTOGRAM_LEVELS_MODE = Literal['linear', 'logarithmic']
THISTOGRAM_SLIDE = Literal['frame', 'replace', 'scroll', 'rscroll', 'picture']

@dataclass
class thistogram(): # thistogram
 width:int = 0
 w:int = 0
 display_mode:THISTOGRAM_DISPLAY_MODE = 'stack'
 d:THISTOGRAM_DISPLAY_MODE = 'stack'
 levels_mode:THISTOGRAM_LEVELS_MODE = 'linear'
 m:THISTOGRAM_LEVELS_MODE = 'linear'
 components:int = 7
 c:int = 7
 bgopacity:float = '0.9'
 b:float = '0.9'
 envelope:bool = False
 e:bool = False
 ecolor:COLORS = "gold"
 ec:COLORS = "gold"
 slide:THISTOGRAM_SLIDE = 'replace' 
 ...




@dataclass
class threshold(): # threshold
 planes:int = 15 
 ...


THUMBNAIL_LOG = Literal['quiet', 'info', 'verbose']

@dataclass
class thumbnail(): # thumbnail
 n:int = 100
 log:THUMBNAIL_LOG = 'info' 
 ...




@dataclass
class tile(): # tile
 layout:IMAGE_SIZES = "6x5"
 nb_frames:int = 0
 margin:int = 0
 padding:int = 0
 color:COLORS = "black"
 overlap:int = 0
 init_padding:int = 0 
 ...


TINTERLACE_MODE = Literal['merge', 'drop_even', 'drop_odd', 'pad', 'interleave_top', 'interleave_bottom', 'interlacex2', 'mergex2']

@dataclass
class tinterlace(): # tinterlace
 mode:TINTERLACE_MODE = 'merge' 
 ...




@dataclass
class tlut2(): # tlut2
 c0:str = "x"
 c1:str = "x"
 c2:str = "x"
 c3:str = "x" 
 ...




@dataclass
class tmedian(): # tmedian
 radius:int = 1
 planes:int = 15
 percentile:float = '0.5' 
 ...




@dataclass
class tmidequalizer(): # tmidequalizer
 radius:int = 5
 sigma:float = '0.5'
 planes:int = 15 
 ...




@dataclass
class tmix(): # tmix
 frames:int = 3
 weights:str = "1 1 1"
 scale:float = '0'
 planes:str = 'F' 
 ...


TONEMAP_TONEMAP = Literal['none', 'linear', 'gamma', 'clip', 'reinhard', 'hable', 'mobius']

@dataclass
class tonemap(): # tonemap
 tonemap:TONEMAP_TONEMAP = 'none'
 param:float = 'nan'
 desat:float = '2'
 peak:float = '0' 
 ...


TPAD_START_MODE = Literal['add', 'clone']

@dataclass
class tpad(): # tpad
 start:int = 0
 stop:int = 0
 start_mode:TPAD_START_MODE = 'add'
 stop_mode:TPAD_START_MODE = 'add'
 start_duration:str = '0'
 stop_duration:str = '0'
 color:COLORS = "black" 
 ...


TRANSPOSE_DIR = Literal['cclock_flip', 'clock', 'cclock', 'clock_flip']
TRANSPOSE_PASSTHROUGH = Literal['none', 'portrait', 'landscape']

@dataclass
class transpose(): # transpose
 dir:TRANSPOSE_DIR = 'cclock_flip'
 passthrough:TRANSPOSE_PASSTHROUGH = 'none' 
 ...




@dataclass
class trim(): # trim
 start:str = 'INT64_MAX'
 starti:str = 'INT64_MAX'
 end:str = 'INT64_MAX'
 endi:str = 'INT64_MAX'
 start_pts:int = 'I64_MIN'
 end_pts:int = 'I64_MIN'
 duration:str = '0'
 durationi:str = '0'
 start_frame:int = -1
 end_frame:int = 'I64_MAX' 
 ...




@dataclass
class unsharp(): # unsharp
 luma_msize_x:int = 5
 lx:int = 5
 luma_msize_y:int = 5
 ly:int = 5
 luma_amount:float = '1'
 la:float = '1'
 chroma_msize_x:int = 5
 cx:int = 5
 chroma_msize_y:int = 5
 cy:int = 5
 chroma_amount:float = '0'
 ca:float = '0'
 alpha_msize_x:int = 5
 ax:int = 5
 alpha_msize_y:int = 5
 ay:int = 5
 alpha_amount:float = '0'
 aa:float = '0' 
 ...




@dataclass
class untile(): # untile
 layout:IMAGE_SIZES = "6x5" 
 ...


V360_INPUT = Literal['e', 'equirect', 'c3x2', 'c6x1', 'eac', 'dfisheye', 'flat', 'rectilinear', 'gnomonic', 'barrel', 'fb', 'c1x6', 'sg', 'mercator', 'ball', 'hammer', 'sinusoidal', 'fisheye', 'pannini', 'cylindrical', 'tetrahedron', 'barrelsplit', 'tsp', 'hequirect', 'he', 'equisolid', 'og', 'octahedron', 'cylindricalea']
V360_OUTPUT = Literal['e', 'equirect', 'c3x2', 'c6x1', 'eac', 'dfisheye', 'flat', 'rectilinear', 'gnomonic', 'barrel', 'fb', 'c1x6', 'sg', 'mercator', 'ball', 'hammer', 'sinusoidal', 'fisheye', 'pannini', 'cylindrical', 'perspective', 'tetrahedron', 'barrelsplit', 'tsp', 'hequirect', 'he', 'equisolid', 'og', 'octahedron', 'cylindricalea']
V360_INTERP = Literal['near', 'nearest', 'line', 'linear', 'lagrange9', 'cube', 'cubic', 'lanc', 'lanczos', 'sp16', 'spline16', 'gauss', 'gaussian', 'mitchell']
V360_IN_STEREO = Literal['2d', 'sbs', 'tb']

@dataclass
class v360(): # v360
 input:V360_INPUT = 'e'
 output:V360_OUTPUT = 'c3x2'
 interp:V360_INTERP = 'line'
 w:int = 0
 h:int = 0
 in_stereo:V360_IN_STEREO = '2d'
 out_stereo:V360_IN_STEREO = '2d'
 in_forder:str = "rludfb"
 out_forder:str = "rludfb"
 in_frot:str = "000000"
 out_frot:str = "000000"
 in_pad:float = '0'
 out_pad:float = '0'
 fin_pad:int = 0
 fout_pad:int = 0
 yaw:float = '0'
 pitch:float = '0'
 roll:float = '0'
 rorder:str = "ypr"
 h_fov:float = '0'
 v_fov:float = '0'
 d_fov:float = '0'
 h_flip:bool = False
 v_flip:bool = False
 d_flip:bool = False
 ih_flip:bool = False
 iv_flip:bool = False
 in_trans:bool = False
 out_trans:bool = False
 ih_fov:float = '0'
 iv_fov:float = '0'
 id_fov:float = '0'
 h_offset:float = '0'
 v_offset:float = '0'
 alpha_mask:bool = False
 reset_rot:bool = False 
 ...


VAGUEDENOISER_METHOD = Literal['hard', 'soft', 'garrote']
VAGUEDENOISER_TYPE = Literal['universal', 'bayes']

@dataclass
class vaguedenoiser(): # vaguedenoiser
 threshold:float = '2'
 method:VAGUEDENOISER_METHOD = 'garrote'
 nsteps:int = 6
 percent:float = '85'
 planes:int = 15
 type:VAGUEDENOISER_TYPE = 'universal' 
 ...




@dataclass
class varblur(): # varblur
 min_r:int = 0
 max_r:int = 8
 planes:int = 15 
 ...


VECTORSCOPE_MODE = Literal['gray', 'tint', 'color', 'color2', 'color3', 'color4', 'color5']
VECTORSCOPE_ENVELOPE = Literal['none', 'instant', 'peak', 'peak+instant']
VECTORSCOPE_GRATICULE = Literal['none', 'green', 'color', 'invert']
VECTORSCOPE_FLAGS = Literal['white', 'black', 'name']
VECTORSCOPE_COLORSPACE = Literal['auto', '601', '709']

@dataclass
class vectorscope(): # vectorscope
 mode:VECTORSCOPE_MODE = 'gray'
 m:VECTORSCOPE_MODE = 'gray'
 x:int = 1
 y:int = 2
 intensity:float = '0.004'
 i:float = '0.004'
 envelope:VECTORSCOPE_ENVELOPE = 'none'
 e:VECTORSCOPE_ENVELOPE = 'none'
 graticule:VECTORSCOPE_GRATICULE = 'none'
 g:VECTORSCOPE_GRATICULE = 'none'
 opacity:float = '0.75'
 o:float = '0.75'
 flags:VECTORSCOPE_FLAGS = 'name'
 f:VECTORSCOPE_FLAGS = 'name'
 bgopacity:float = '0.3'
 b:float = '0.3'
 lthreshold:float = '0'
 l:float = '0'
 hthreshold:float = '1'
 h:float = '1'
 colorspace:VECTORSCOPE_COLORSPACE = 'auto'
 c:VECTORSCOPE_COLORSPACE = 'auto'
 tint0:float = '0'
 t0:float = '0'
 tint1:float = '0'
 t1:float = '0' 
 ...




@dataclass
class vflip(): # vflip 
 ...




@dataclass
class vibrance(): # vibrance
 intensity:float = '0'
 rbal:float = '1'
 gbal:float = '1'
 bbal:float = '1'
 rlum:float = '0.072186'
 glum:float = '0.715158'
 blum:float = '0.212656'
 alternate:bool = False 
 ...




@dataclass
class vidstabdetect(): # vidstabdetect
 result:str = "transforms.trf"
 shakiness:int = 5
 accuracy:int = 15
 stepsize:int = 6
 mincontrast:float = '0.25'
 show:int = 0
 tripod:int = 0 
 ...


VIDSTABTRANSFORM_OPTALGO = Literal['opt', 'gauss', 'avg']
VIDSTABTRANSFORM_CROP = Literal['keep', 'black']
VIDSTABTRANSFORM_INTERPOL = Literal['no', 'linear', 'bilinear', 'bicubic']

@dataclass
class vidstabtransform(): # vidstabtransform
 input:str = "transforms.trf"
 smoothing:int = 15
 optalgo:VIDSTABTRANSFORM_OPTALGO = 'opt'
 maxshift:int = -1
 maxangle:float = '-1'
 crop:VIDSTABTRANSFORM_CROP = 'keep'
 invert:int = 0
 relative:int = 1
 zoom:float = '0'
 optzoom:int = 1
 zoomspeed:float = '0.25'
 interpol:VIDSTABTRANSFORM_INTERPOL = 'bilinear'
 tripod:bool = False
 debug:bool = False 
 ...




@dataclass
class vif(): # vif 
 ...


VIGNETTE_MODE = Literal['forward', 'backward']
VIGNETTE_EVAL = Literal['init', 'frame']

@dataclass
class vignette(): # vignette
 angle:str = "PI/5"
 a:str = "PI/5"
 x0:str = "w/2"
 y0:str = "h/2"
 mode:VIGNETTE_MODE = 'forward'
 eval:VIGNETTE_EVAL = 'init'
 dither:bool = True
 aspect:float|str = '1/1' 
 ...




@dataclass
class vmafmotion(): # vmafmotion
 stats_file:str = None 
 ...


W3FDIF_FILTER = Literal['simple', 'complex']
W3FDIF_MODE = Literal['frame', 'field']
W3FDIF_PARITY = Literal['tff', 'bff', 'auto']
W3FDIF_DEINT = Literal['all', 'interlaced']

@dataclass
class w3fdif(): # w3fdif
 filter:W3FDIF_FILTER = 'complex'
 mode:W3FDIF_MODE = 'field'
 parity:W3FDIF_PARITY = 'auto'
 deint:W3FDIF_DEINT = 'all' 
 ...


WAVEFORM_MODE = Literal['row', 'column']
WAVEFORM_DISPLAY = Literal['overlay', 'stack', 'parade']
WAVEFORM_ENVELOPE = Literal['none', 'instant', 'peak', 'peak+instant']
WAVEFORM_FILTER = Literal['lowpass', 'flat', 'aflat', 'chroma', 'color', 'acolor', 'xflat', 'yflat']
WAVEFORM_GRATICULE = Literal['none', 'green', 'orange', 'invert']
WAVEFORM_FLAGS = Literal['numbers', 'dots']
WAVEFORM_SCALE = Literal['digital', 'millivolts', 'ire']
WAVEFORM_FITMODE = Literal['none', 'size']

@dataclass
class waveform(): # waveform
 mode:WAVEFORM_MODE = 'column'
 m:WAVEFORM_MODE = 'column'
 intensity:float = '0.04'
 i:float = '0.04'
 mirror:bool = True
 r:bool = True
 display:WAVEFORM_DISPLAY = 'stack'
 d:WAVEFORM_DISPLAY = 'stack'
 components:int = 1
 c:int = 1
 envelope:WAVEFORM_ENVELOPE = 'none'
 e:WAVEFORM_ENVELOPE = 'none'
 filter:WAVEFORM_FILTER = 'lowpass'
 f:WAVEFORM_FILTER = 'lowpass'
 graticule:WAVEFORM_GRATICULE = 'none'
 g:WAVEFORM_GRATICULE = 'none'
 opacity:float = '0.75'
 o:float = '0.75'
 flags:WAVEFORM_FLAGS = 'numbers'
 fl:WAVEFORM_FLAGS = 'numbers'
 scale:WAVEFORM_SCALE = 'digital'
 s:WAVEFORM_SCALE = 'digital'
 bgopacity:float = '0.75'
 b:float = '0.75'
 tint0:float = '0'
 t0:float = '0'
 tint1:float = '0'
 t1:float = '0'
 fitmode:WAVEFORM_FITMODE = 'none'
 fm:WAVEFORM_FITMODE = 'none' 
 ...




@dataclass
class xbr(): # xbr
 n:int = 3 
 ...


XCORRELATE_SECONDARY = Literal['first', 'all']

@dataclass
class xcorrelate(): # xcorrelate
 planes:int = 7
 secondary:XCORRELATE_SECONDARY = 'all' 
 ...


XFADE_TRANSITION = Literal['custom', 'fade', 'wipeleft', 'wiperight', 'wipeup', 'wipedown', 'slideleft', 'slideright', 'slideup', 'slidedown', 'circlecrop', 'rectcrop', 'distance', 'fadeblack', 'fadewhite', 'radial', 'smoothleft', 'smoothright', 'smoothup', 'smoothdown', 'circleopen', 'circleclose', 'vertopen', 'vertclose', 'horzopen', 'horzclose', 'dissolve', 'pixelize', 'diagtl', 'diagtr', 'diagbl', 'diagbr', 'hlslice', 'hrslice', 'vuslice', 'vdslice', 'hblur', 'fadegrays', 'wipetl', 'wipetr', 'wipebl', 'wipebr', 'squeezeh', 'squeezev', 'zoomin', 'fadefast', 'fadeslow']

@dataclass
class xfade(): # xfade
 transition:XFADE_TRANSITION = 'fade'
 duration:str = '1'
 offset:str = '0'
 expr:str = None 
 ...




@dataclass
class xmedian(): # xmedian
 inputs:int = 3
 planes:int = 15
 percentile:float = '0.5' 
 ...




@dataclass
class xstack(): # xstack
 inputs:int = 2
 layout:str = None
 grid:IMAGE_SIZES = None
 shortest:bool = False
 fill:str = "none" 
 ...


YADIF_MODE = Literal['send_frame', 'send_field', 'send_frame_nospatial', 'send_field_nospatial']
YADIF_PARITY = Literal['tff', 'bff', 'auto']
YADIF_DEINT = Literal['all', 'interlaced']

@dataclass
class yadif(): # yadif
 mode:YADIF_MODE = 'send_frame'
 parity:YADIF_PARITY = 'auto'
 deint:YADIF_DEINT = 'all' 
 ...


YADIF_VIDEOTOOLBOX_MODE = Literal['send_frame', 'send_field', 'send_frame_nospatial', 'send_field_nospatial']
YADIF_VIDEOTOOLBOX_PARITY = Literal['tff', 'bff', 'auto']
YADIF_VIDEOTOOLBOX_DEINT = Literal['all', 'interlaced']

@dataclass
class yadif_videotoolbox(): # yadif_videotoolbox
 mode:YADIF_VIDEOTOOLBOX_MODE = 'send_frame'
 parity:YADIF_VIDEOTOOLBOX_PARITY = 'auto'
 deint:YADIF_VIDEOTOOLBOX_DEINT = 'all' 
 ...




@dataclass
class yaepblur(): # yaepblur
 radius:int = 3
 r:int = 3
 planes:int = 1
 p:int = 1
 sigma:int = 128
 s:int = 128 
 ...




@dataclass
class zoompan(): # zoompan
 zoom:str = "1"
 z:str = "1"
 x:str = "0"
 y:str = "0"
 d:str = "90"
 s:IMAGE_SIZES = "hd720"
 fps:VIDEO_RATES = "25" 
 ...


ZSCALE_DITHER = Literal['none', 'ordered', 'random', 'error_diffusion']
ZSCALE_FILTER = Literal['point', 'bilinear', 'bicubic', 'spline16', 'spline36', 'lanczos']
ZSCALE_OUT_RANGE = Literal['input', 'limited', 'full', 'unknown', 'tv', 'pc']
ZSCALE_PRIMARIES = Literal['input', '709', 'unspecified', '170m', '240m', '2020', 'unknown', 'bt709', 'bt470m', 'bt470bg', 'smpte170m', 'smpte240m', 'film', 'bt2020', 'smpte428', 'smpte431', 'smpte432', 'jedec-p22', 'ebu3213']
ZSCALE_TRANSFER = Literal['input', '709', 'unspecified', '601', 'linear', '2020_10', '2020_12', 'unknown', 'bt470m', 'bt470bg', 'smpte170m', 'smpte240m', 'bt709', 'linear', 'log100', 'log316', 'bt2020-10', 'bt2020-12', 'smpte2084', 'iec61966-2-4', 'iec61966-2-1', 'arib-std-b67']
ZSCALE_MATRIX = Literal['input', '709', 'unspecified', '470bg', '170m', '2020_ncl', '2020_cl', 'unknown', 'gbr', 'bt709', 'fcc', 'bt470bg', 'smpte170m', 'smpte240m', 'ycgco', 'bt2020nc', 'bt2020c', 'chroma-derived-nc', 'chroma-derived-c', 'ictcp']
ZSCALE_CHROMAL = Literal['input', 'left', 'center', 'topleft', 'top', 'bottomleft', 'bottom']

@dataclass
class zscale(): # zscale
 w:str = None
 width:str = None
 h:str = None
 height:str = None
 size:str = None
 s:str = None
 dither:ZSCALE_DITHER = 'none'
 d:ZSCALE_DITHER = 'none'
 filter:ZSCALE_FILTER = 'bilinear'
 f:ZSCALE_FILTER = 'bilinear'
 out_range:ZSCALE_OUT_RANGE = 'input'
 range:ZSCALE_OUT_RANGE = 'input'
 r:ZSCALE_OUT_RANGE = 'input'
 primaries:ZSCALE_PRIMARIES = 'input'
 p:ZSCALE_PRIMARIES = 'input'
 transfer:ZSCALE_TRANSFER = 'input'
 t:ZSCALE_TRANSFER = 'input'
 matrix:ZSCALE_MATRIX = 'input'
 m:ZSCALE_MATRIX = 'input'
 in_range:ZSCALE_OUT_RANGE = 'input'
 rangein:ZSCALE_OUT_RANGE = 'input'
 rin:ZSCALE_OUT_RANGE = 'input'
 primariesin:ZSCALE_PRIMARIES = 'input'
 pin:ZSCALE_PRIMARIES = 'input'
 transferin:ZSCALE_TRANSFER = 'input'
 tin:ZSCALE_TRANSFER = 'input'
 matrixin:ZSCALE_MATRIX = 'input'
 min:ZSCALE_MATRIX = 'input'
 chromal:ZSCALE_CHROMAL = 'input'
 c:ZSCALE_CHROMAL = 'input'
 chromalin:ZSCALE_CHROMAL = 'input'
 cin:ZSCALE_CHROMAL = 'input'
 npl:float = 'nan'
 agamma:bool = True
 param_a:float = 'nan'
 param_b:float = 'nan' 
 ...




@dataclass
class allyuv_allrgb(): # allyuv/allrgb
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1' 
 ...




@dataclass
class cellauto(): # cellauto
 filename:str = None
 f:str = None
 pattern:str = None
 p:str = None
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 size:IMAGE_SIZES = None
 s:IMAGE_SIZES = None
 rule:int = 110
 random_fill_ratio:float = '0.618034'
 ratio:float = '0.618034'
 random_seed:int = -1
 seed:int = -1
 scroll:bool = True
 start_full:bool = False
 full:bool = True
 stitch:bool = True 
 ...




@dataclass
class color(): # color
 color:COLORS = "black"
 c:COLORS = "black"
 size:IMAGE_SIZES = "320x240"
 s:IMAGE_SIZES = "320x240"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1' 
 ...


COLORCHART_PRESET = Literal['reference', 'skintones']

@dataclass
class colorchart(): # colorchart
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1'
 patch_size:IMAGE_SIZES = "64x64"
 preset:COLORCHART_PRESET = 'reference' 
 ...


COLORSPECTRUM_TYPE = Literal['black', 'white', 'all']

@dataclass
class colorspectrum(): # colorspectrum
 size:IMAGE_SIZES = "320x240"
 s:IMAGE_SIZES = "320x240"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1'
 type:COLORSPECTRUM_TYPE = 'black' 
 ...




@dataclass
class coreimagesrc(): # coreimagesrc
 size:IMAGE_SIZES = "320x240"
 s:IMAGE_SIZES = "320x240"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1'
 list_filters:bool = False
 list_generators:bool = False
 filter:str = None
 output_rect:str = None 
 ...




@dataclass
class frei0r_src(): # frei0r_src
 size:IMAGE_SIZES = "320x240"
 framerate:VIDEO_RATES = "25"
 filter_name:str = None
 filter_params:str = None 
 ...


GRADIENTS_TYPE = Literal['linear', 'radial', 'circular', 'spiral']

@dataclass
class gradients(): # gradients
 size:IMAGE_SIZES = "640x480"
 s:IMAGE_SIZES = "640x480"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 c0:COLORS = "random"
 c1:COLORS = "random"
 c2:COLORS = "random"
 c3:COLORS = "random"
 c4:COLORS = "random"
 c5:COLORS = "random"
 c6:COLORS = "random"
 c7:COLORS = "random"
 x0:int = -1
 y0:int = -1
 x1:int = -1
 y1:int = -1
 nb_colors:int = 2
 n:int = 2
 seed:int = -1
 duration:str = '-0.000001'
 d:str = '-0.000001'
 speed:float = '0.01'
 type:GRADIENTS_TYPE = 'linear'
 t:GRADIENTS_TYPE = 'linear' 
 ...




@dataclass
class haldclutsrc(): # haldclutsrc
 level:int = 6
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1' 
 ...




@dataclass
class life(): # life
 filename:str = None
 f:str = None
 size:IMAGE_SIZES = None
 s:IMAGE_SIZES = None
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 rule:str = "B3/S23"
 random_fill_ratio:float = '0.618034'
 ratio:float = '0.618034'
 random_seed:int = -1
 seed:int = -1
 stitch:bool = True
 mold:int = 0
 life_color:COLORS = "white"
 death_color:COLORS = "black"
 mold_color:COLORS = "black" 
 ...


MANDELBROT_OUTER = Literal['iteration_count', 'normalized_iteration_count', 'white', 'outz']
MANDELBROT_INNER = Literal['black', 'period', 'convergence', 'mincol']

@dataclass
class mandelbrot(): # mandelbrot
 size:IMAGE_SIZES = "640x480"
 s:IMAGE_SIZES = "640x480"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 maxiter:int = 7189
 start_x:float = '-0.743644'
 start_y:float = '-0.131826'
 start_scale:float = '3'
 end_scale:float = '0.3'
 end_pts:float = '400'
 bailout:float = '10'
 morphxf:float = '0.01'
 morphyf:float = '0.0123'
 morphamp:float = '0'
 outer:MANDELBROT_OUTER = 'normalized_iteration_count'
 inner:MANDELBROT_INNER = 'mincol' 
 ...


MPTESTSRC_TEST = Literal['dc_luma', 'dc_chroma', 'freq_luma', 'freq_chroma', 'amp_luma', 'amp_chroma', 'cbp', 'mv', 'ring1', 'ring2', 'all']

@dataclass
class mptestsrc(): # mptestsrc
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 test:MPTESTSRC_TEST = 'all'
 t:MPTESTSRC_TEST = 'all'
 max_frames:int = 30
 m:int = 30 
 ...




@dataclass
class nullsrc_yuvtestsrc(): # nullsrc/yuvtestsrc
 size:IMAGE_SIZES = "320x240"
 s:IMAGE_SIZES = "320x240"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1' 
 ...




@dataclass
class pal_75_100_bars(): # pal(75|100)bars
 size:IMAGE_SIZES = "320x240"
 s:IMAGE_SIZES = "320x240"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1' 
 ...




@dataclass
class rgbtestsrc(): # rgbtestsrc
 size:IMAGE_SIZES = "320x240"
 s:IMAGE_SIZES = "320x240"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1'
 complement:bool = False
 co:bool = False 
 ...


SIERPINSKI_TYPE = Literal['carpet', 'triangle']

@dataclass
class sierpinski(): # sierpinski
 size:IMAGE_SIZES = "640x480"
 s:IMAGE_SIZES = "640x480"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 seed:int = -1
 jump:int = 100
 type:SIERPINSKI_TYPE = 'carpet' 
 ...




@dataclass
class smpte_hd_bars(): # smpte(hd)bars
 size:IMAGE_SIZES = "320x240"
 s:IMAGE_SIZES = "320x240"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1' 
 ...




@dataclass
class testsrc(): # testsrc
 size:IMAGE_SIZES = "320x240"
 s:IMAGE_SIZES = "320x240"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1'
 decimals:int = 0
 n:int = 0 
 ...




@dataclass
class testsrc2(): # testsrc2
 size:IMAGE_SIZES = "320x240"
 s:IMAGE_SIZES = "320x240"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 duration:str = '-0.000001'
 d:str = '-0.000001'
 sar:float|str = '1/1'
 alpha:int = 255 
 ...




@dataclass
class a3dscope(): # a3dscope
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 size:IMAGE_SIZES = "hd720"
 s:IMAGE_SIZES = "hd720"
 fov:float = '90'
 roll:float = '0'
 pitch:float = '0'
 yaw:float = '0'
 xzoom:float = '1'
 yzoom:float = '1'
 zzoom:float = '1'
 xpos:float = '0'
 ypos:float = '0'
 zpos:float = '0'
 length:int = 15 
 ...


ABITSCOPE_MODE = Literal['bars', 'trace']

@dataclass
class abitscope(): # abitscope
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 size:IMAGE_SIZES = "1024x256"
 s:IMAGE_SIZES = "1024x256"
 colors:str = "red|green|blue|yellow|orange|lime|pink|magenta|brown"
 mode:ABITSCOPE_MODE = 'bars'
 m:ABITSCOPE_MODE = 'bars' 
 ...


AHISTOGRAM_DMODE = Literal['single', 'separate']
AHISTOGRAM_SCALE = Literal['log', 'sqrt', 'cbrt', 'lin', 'rlog']
AHISTOGRAM_ASCALE = Literal['log', 'lin']
AHISTOGRAM_SLIDE = Literal['replace', 'scroll']
AHISTOGRAM_HMODE = Literal['abs', 'sign']

@dataclass
class ahistogram(): # ahistogram
 dmode:AHISTOGRAM_DMODE = 'single'
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 size:IMAGE_SIZES = "hd720"
 s:IMAGE_SIZES = "hd720"
 scale:AHISTOGRAM_SCALE = 'log'
 ascale:AHISTOGRAM_ASCALE = 'log'
 acount:int = 1
 rheight:float = '0.1'
 slide:AHISTOGRAM_SLIDE = 'replace'
 hmode:AHISTOGRAM_HMODE = 'abs' 
 ...




@dataclass
class aphasemeter(): # aphasemeter
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 size:IMAGE_SIZES = "800x400"
 s:IMAGE_SIZES = "800x400"
 rc:int = 2
 gc:int = 7
 bc:int = 1
 mpc:str = "none"
 video:bool = True
 phasing:bool = False
 tolerance:float = '0'
 t:float = '0'
 angle:float = '170'
 a:float = '170'
 duration:str = '2'
 d:str = '2' 
 ...


AVECTORSCOPE_MODE = Literal['lissajous', 'lissajous_xy', 'polar']
AVECTORSCOPE_DRAW = Literal['dot', 'line', 'aaline']
AVECTORSCOPE_SCALE = Literal['lin', 'sqrt', 'cbrt', 'log']
AVECTORSCOPE_MIRROR = Literal['none', 'x', 'y', 'xy']

@dataclass
class avectorscope(): # avectorscope
 mode:AVECTORSCOPE_MODE = 'lissajous'
 m:AVECTORSCOPE_MODE = 'lissajous'
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 size:IMAGE_SIZES = "400x400"
 s:IMAGE_SIZES = "400x400"
 rc:int = 40
 gc:int = 160
 bc:int = 80
 ac:int = 255
 rf:int = 15
 gf:int = 10
 bf:int = 5
 af:int = 5
 zoom:float = '1'
 draw:AVECTORSCOPE_DRAW = 'dot'
 scale:AVECTORSCOPE_SCALE = 'lin'
 swap:bool = True
 mirror:AVECTORSCOPE_MIRROR = 'none' 
 ...




@dataclass
class concat(): # concat
 n:int = 2
 v:int = 1
 a:int = 0
 unsafe:bool = False 
 ...


SHOWCQT_CSP = Literal['unspecified', 'bt709', 'fcc', 'bt470bg', 'smpte170m', 'smpte240m', 'bt2020ncl']

@dataclass
class showcqt(): # showcqt
 size:IMAGE_SIZES = "1920x1080"
 s:IMAGE_SIZES = "1920x1080"
 fps:VIDEO_RATES = "25"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 bar_h:int = -1
 axis_h:int = -1
 sono_h:int = -1
 fullhd:bool = True
 sono_v:str = "16"
 volume:str = "16"
 bar_v:str = "sono_v"
 volume2:str = "sono_v"
 sono_g:float = '3'
 gamma:float = '3'
 bar_g:float = '1'
 gamma2:float = '1'
 bar_t:float = '1'
 timeclamp:float = '0.17'
 tc:float = '0.17'
 attack:float = '0'
 basefreq:float = '20.0152'
 endfreq:float = '20495.6'
 coeffclamp:float = '1'
 tlength:str = None
 count:int = 6
 fcount:int = 0
 fontfile:str = None
 font:str = None
 fontcolor:str = None
 axisfile:str = None
 axis:bool = True
 text:bool = True
 csp:SHOWCQT_CSP = 'unspecified'
 cscheme:str = "1|0.5|0|0|0.5|1" 
 ...


SHOWCWT_SCALE = Literal['linear', 'log2', 'bark', 'mel', 'erbs']
SHOWCWT_MODE = Literal['magnitude', 'phase', 'magphase', 'channel', 'stereo']
SHOWCWT_SLIDE = Literal['replace', 'scroll', 'frame']
SHOWCWT_DIRECTION = Literal['lr', 'rl', 'ud', 'du']

@dataclass
class showcwt(): # showcwt
 size:IMAGE_SIZES = "640x512"
 s:IMAGE_SIZES = "640x512"
 rate:str = "25"
 r:str = "25"
 scale:SHOWCWT_SCALE = 'linear'
 min:float = '20'
 max:float = '20000'
 logb:float = '0.0001'
 deviation:float = '1'
 pps:int = 64
 mode:SHOWCWT_MODE = 'magnitude'
 slide:SHOWCWT_SLIDE = 'replace'
 direction:SHOWCWT_DIRECTION = 'lr' 
 ...


SHOWFREQS_MODE = Literal['line', 'bar', 'dot']
SHOWFREQS_ASCALE = Literal['lin', 'sqrt', 'cbrt', 'log']
SHOWFREQS_FSCALE = Literal['lin', 'log', 'rlog']
SHOWFREQS_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']
SHOWFREQS_CMODE = Literal['combined', 'separate']
SHOWFREQS_DATA = Literal['magnitude', 'phase', 'delay']

@dataclass
class showfreqs(): # showfreqs
 size:IMAGE_SIZES = "1024x512"
 s:IMAGE_SIZES = "1024x512"
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 mode:SHOWFREQS_MODE = 'bar'
 ascale:SHOWFREQS_ASCALE = 'log'
 fscale:SHOWFREQS_FSCALE = 'lin'
 win_size:int = 2048
 win_func:SHOWFREQS_WIN_FUNC = 'hann'
 overlap:float = '1'
 averaging:int = 1
 colors:str = "red|green|blue|yellow|orange|lime|pink|magenta|brown"
 cmode:SHOWFREQS_CMODE = 'combined'
 minamp:float = '1e-06'
 data:SHOWFREQS_DATA = 'magnitude'
 channels:str = "all" 
 ...


SHOWSPATIAL_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']

@dataclass
class showspatial(): # showspatial
 size:IMAGE_SIZES = "512x512"
 s:IMAGE_SIZES = "512x512"
 win_size:int = 4096
 win_func:SHOWSPATIAL_WIN_FUNC = 'hann'
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25" 
 ...


SHOWSPECTRUM_SLIDE = Literal['replace', 'scroll', 'fullframe', 'rscroll', 'lreplace']
SHOWSPECTRUM_MODE = Literal['combined', 'separate']
SHOWSPECTRUM_COLOR = Literal['channel', 'intensity', 'rainbow', 'moreland', 'nebulae', 'fire', 'fiery', 'fruit', 'cool', 'magma', 'green', 'viridis', 'plasma', 'cividis', 'terrain']
SHOWSPECTRUM_SCALE = Literal['lin', 'sqrt', 'cbrt', 'log', '4thrt', '5thrt']
SHOWSPECTRUM_FSCALE = Literal['lin', 'log']
SHOWSPECTRUM_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']
SHOWSPECTRUM_ORIENTATION = Literal['vertical', 'horizontal']
SHOWSPECTRUM_DATA = Literal['magnitude', 'phase', 'uphase']

@dataclass
class showspectrum(): # showspectrum
 size:IMAGE_SIZES = "640x512"
 s:IMAGE_SIZES = "640x512"
 slide:SHOWSPECTRUM_SLIDE = 'replace'
 mode:SHOWSPECTRUM_MODE = 'combined'
 color:SHOWSPECTRUM_COLOR = 'channel'
 scale:SHOWSPECTRUM_SCALE = 'sqrt'
 fscale:SHOWSPECTRUM_FSCALE = 'lin'
 saturation:float = '1'
 win_func:SHOWSPECTRUM_WIN_FUNC = 'hann'
 orientation:SHOWSPECTRUM_ORIENTATION = 'vertical'
 overlap:float = '0'
 gain:float = '1'
 data:SHOWSPECTRUM_DATA = 'magnitude'
 rotation:float = '0'
 start:int = 0
 stop:int = 0
 fps:str = "auto"
 legend:bool = False
 drange:float = '120'
 limit:float = '0'
 opacity:float = '1' 
 ...


SHOWSPECTRUMPIC_MODE = Literal['combined', 'separate']
SHOWSPECTRUMPIC_COLOR = Literal['channel', 'intensity', 'rainbow', 'moreland', 'nebulae', 'fire', 'fiery', 'fruit', 'cool', 'magma', 'green', 'viridis', 'plasma', 'cividis', 'terrain']
SHOWSPECTRUMPIC_SCALE = Literal['lin', 'sqrt', 'cbrt', 'log', '4thrt', '5thrt']
SHOWSPECTRUMPIC_FSCALE = Literal['lin', 'log']
SHOWSPECTRUMPIC_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']
SHOWSPECTRUMPIC_ORIENTATION = Literal['vertical', 'horizontal']

@dataclass
class showspectrumpic(): # showspectrumpic
 size:IMAGE_SIZES = "4096x2048"
 s:IMAGE_SIZES = "4096x2048"
 mode:SHOWSPECTRUMPIC_MODE = 'combined'
 color:SHOWSPECTRUMPIC_COLOR = 'intensity'
 scale:SHOWSPECTRUMPIC_SCALE = 'log'
 fscale:SHOWSPECTRUMPIC_FSCALE = 'lin'
 saturation:float = '1'
 win_func:SHOWSPECTRUMPIC_WIN_FUNC = 'hann'
 orientation:SHOWSPECTRUMPIC_ORIENTATION = 'vertical'
 gain:float = '1'
 legend:bool = True
 rotation:float = '0'
 start:int = 0
 stop:int = 0
 drange:float = '120'
 limit:float = '0'
 opacity:float = '1' 
 ...


SHOWVOLUME_O = Literal['h', 'v']
SHOWVOLUME_M = Literal['p', 'r']
SHOWVOLUME_DS = Literal['lin', 'log']

@dataclass
class showvolume(): # showvolume
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 b:int = 1
 w:int = 400
 h:int = 20
 f:float = '0.95'
 c:str = None
 t:bool = True
 v:bool = True
 dm:float = '0'
 dmc:COLORS = "orange"
 o:SHOWVOLUME_O = 'h'
 s:int = 0
 p:float = '0'
 m:SHOWVOLUME_M = 'p'
 ds:SHOWVOLUME_DS = 'lin' 
 ...


SHOWWAVES_MODE = Literal['point', 'line', 'p2p', 'cline']
SHOWWAVES_SCALE = Literal['lin', 'log', 'sqrt', 'cbrt']
SHOWWAVES_DRAW = Literal['scale', 'full']

@dataclass
class showwaves(): # showwaves
 size:IMAGE_SIZES = "600x240"
 s:IMAGE_SIZES = "600x240"
 mode:SHOWWAVES_MODE = 'point'
 n:int = 0
 rate:VIDEO_RATES = "25"
 r:VIDEO_RATES = "25"
 split_channels:bool = False
 colors:str = "red|green|blue|yellow|orange|lime|pink|magenta|brown"
 scale:SHOWWAVES_SCALE = 'lin'
 draw:SHOWWAVES_DRAW = 'scale' 
 ...


SHOWWAVESPIC_SCALE = Literal['lin', 'log', 'sqrt', 'cbrt']
SHOWWAVESPIC_DRAW = Literal['scale', 'full']
SHOWWAVESPIC_FILTER = Literal['average', 'peak']

@dataclass
class showwavespic(): # showwavespic
 size:IMAGE_SIZES = "600x240"
 s:IMAGE_SIZES = "600x240"
 split_channels:bool = False
 colors:str = "red|green|blue|yellow|orange|lime|pink|magenta|brown"
 scale:SHOWWAVESPIC_SCALE = 'lin'
 draw:SHOWWAVESPIC_DRAW = 'scale'
 filter:SHOWWAVESPIC_FILTER = 'average' 
 ...


SPECTRUMSYNTH_SCALE = Literal['lin', 'log']
SPECTRUMSYNTH_SLIDE = Literal['replace', 'scroll', 'fullframe', 'rscroll']
SPECTRUMSYNTH_WIN_FUNC = Literal['rect', 'bartlett', 'hann', 'hanning', 'hamming', 'blackman', 'welch', 'flattop', 'bharris', 'bnuttall', 'bhann', 'sine', 'nuttall', 'lanczos', 'gauss', 'tukey', 'dolph', 'cauchy', 'parzen', 'poisson', 'bohman', 'kaiser']
SPECTRUMSYNTH_ORIENTATION = Literal['vertical', 'horizontal']

@dataclass
class spectrumsynth(): # spectrumsynth
 sample_rate:int = 44100
 channels:int = 1
 scale:SPECTRUMSYNTH_SCALE = 'log'
 slide:SPECTRUMSYNTH_SLIDE = 'fullframe'
 win_func:SPECTRUMSYNTH_WIN_FUNC = 'rect'
 overlap:float = '1'
 orientation:SPECTRUMSYNTH_ORIENTATION = 'vertical' 
 ...




@dataclass
class avsynctest(): # avsynctest
 size:IMAGE_SIZES = "hd720"
 s:IMAGE_SIZES = "hd720"
 framerate:VIDEO_RATES = "30"
 fr:VIDEO_RATES = "30"
 samplerate:int = 44100
 sr:int = 44100
 amplitude:float = '0.7'
 a:float = '0.7'
 period:int = 3
 p:int = 3
 delay:int = 0
 dl:int = 0
 cycle:bool = False
 c:bool = False
 duration:str = '0'
 d:str = '0'
 fg:COLORS = "white"
 bg:COLORS = "black"
 ag:COLORS = "gray" 
 ...




@dataclass
class _a_movie(): # (a)movie
 filename:str = None
 format_name:str = None
 f:str = None
 stream_index:int = -1
 si:int = -1
 seek_point:float = '0'
 sp:float = '0'
 streams:str = None
 s:str = None
 loop:int = 1
 discontinuity:str = '0'
 dec_threads:int = 0
 format_opts:dict = None 
 ...




@dataclass
class abuffer(): # abuffer
 time_base:float|str = '0/1'
 sample_rate:int = 0
 sample_fmt:SAMPLE_RMT = 'none'
 channel_layout:str = None
 channels:int = 0 
 ...




@dataclass
class buffer(): # buffer
 width:int = 0
 video_size:IMAGE_SIZES = None
 height:int = 0
 pix_fmt:PIXEL_FORMATS = 'none'
 sar:float|str = '0/1'
 pixel_aspect:float|str = '0/1'
 time_base:float|str = '0/1'
 frame_rate:float|str = '0/1' 
 ...




@dataclass
class abuffersink(): # abuffersink
 sample_fmts:str = None
 sample_rates:str = None
 channel_layouts:str = None
 channel_counts:str = None
 ch_layouts:str = None
 all_channel_counts:bool = False 
 ...




@dataclass
class buffersink(): # buffersink
 pix_fmts:str = None 
 ...


AV1_METADATA_BSF_TD = Literal['pass', 'insert', 'remove']
AV1_METADATA_BSF_COLOR_RANGE = Literal['tv', 'pc']
AV1_METADATA_BSF_CHROMA_SAMPLE_POSITION = Literal['unknown', 'vertical', 'colocated']

@dataclass
class av1_metadata_bsf(): # av1_metadata_bsf
 td:AV1_METADATA_BSF_TD = 'pass'
 color_primaries:int = -1
 transfer_characteristics:int = -1
 matrix_coefficients:int = -1
 color_range:AV1_METADATA_BSF_COLOR_RANGE = '-1'
 chroma_sample_position:AV1_METADATA_BSF_CHROMA_SAMPLE_POSITION = '-1'
 tick_rate:float|str = '0/1'
 num_ticks_per_picture:int = -1
 delete_padding:bool = False 
 ...


DUMP_EXTRADATA_BSF_FREQ = Literal['k', 'keyframe', 'e', 'all']

@dataclass
class dump_extradata_bsf(): # dump_extradata bsf
 freq:DUMP_EXTRADATA_BSF_FREQ = 'k' 
 ...


DV_ERROR_MARKER_STA = Literal['ok', 'Aa', 'Ba', 'Ca', 'erri', 'erru', 'err', 'Ab', 'Bb', 'Cb', 'A', 'B', 'C', 'a', 'b', 'res', 'notok', 'notres']

@dataclass
class dv_error_marker(): # dv_error_marker
 color:COLORS = "yellow"
 sta:DV_ERROR_MARKER_STA = 'Aa+Ba+Ca+erri+erru+err+Ab+Bb+Cb+A+B+C+a+b+res+notok+notres' 
 ...




@dataclass
class extract_extradata(): # extract_extradata
 remove:int = 0 
 ...




@dataclass
class filter_units(): # filter_units
 pass_types:str = None
 remove_types:str = None 
 ...


H264_METADATA_BSF_AUD = Literal['pass', 'insert', 'remove']
H264_METADATA_BSF_DISPLAY_ORIENTATION = Literal['pass', 'insert', 'remove', 'extract']
H264_METADATA_BSF_FLIP = Literal['horizontal', 'vertical']
H264_METADATA_BSF_LEVEL = Literal['auto', '1', '1b', '1.1', '1.2', '1.3', '2', '2.1', '2.2', '3', '3.1', '3.2', '4', '4.1', '4.2', '5', '5.1', '5.2', '6', '6.1', '6.2']

@dataclass
class h264_metadata_bsf(): # h264_metadata_bsf
 aud:H264_METADATA_BSF_AUD = 'pass'
 sample_aspect_ratio:float|str = '0/1'
 overscan_appropriate_flag:int = -1
 video_format:int = -1
 video_full_range_flag:int = -1
 colour_primaries:int = -1
 transfer_characteristics:int = -1
 matrix_coefficients:int = -1
 chroma_sample_loc_type:int = -1
 tick_rate:float|str = '0/1'
 fixed_frame_rate_flag:int = -1
 zero_new_constraint_set_flags:bool = False
 crop_left:int = -1
 crop_right:int = -1
 crop_top:int = -1
 crop_bottom:int = -1
 sei_user_data:str = None
 delete_filler:int = 0
 display_orientation:H264_METADATA_BSF_DISPLAY_ORIENTATION = 'pass'
 rotate:float = 'nan'
 flip:H264_METADATA_BSF_FLIP = '0'
 level:H264_METADATA_BSF_LEVEL = '-2' 
 ...


HAPQA_EXTRACT_BSF_TEXTURE = Literal['color', 'alpha']

@dataclass
class hapqa_extract_bsf(): # hapqa_extract_bsf
 texture:HAPQA_EXTRACT_BSF_TEXTURE = 'color' 
 ...


H265_METADATA_BSF_AUD = Literal['pass', 'insert', 'remove']
H265_METADATA_BSF_LEVEL = Literal['auto', '1', '2', '2.1', '3', '3.1', '4', '4.1', '5', '5.1', '5.2', '6', '6.1', '6.2', '8.5']

@dataclass
class h265_metadata_bsf(): # h265_metadata_bsf
 aud:H265_METADATA_BSF_AUD = 'pass'
 sample_aspect_ratio:float|str = '0/1'
 video_format:int = -1
 video_full_range_flag:int = -1
 colour_primaries:int = -1
 transfer_characteristics:int = -1
 matrix_coefficients:int = -1
 chroma_sample_loc_type:int = -1
 tick_rate:float|str = '0/1'
 num_ticks_poc_diff_one:int = -1
 crop_left:int = -1
 crop_right:int = -1
 crop_top:int = -1
 crop_bottom:int = -1
 level:H265_METADATA_BSF_LEVEL = '-2' 
 ...




@dataclass
class mpeg2_metadata_bsf(): # mpeg2_metadata_bsf
 display_aspect_ratio:float|str = '0/1'
 frame_rate:float|str = '0/1'
 video_format:int = -1
 colour_primaries:int = -1
 transfer_characteristics:int = -1
 matrix_coefficients:int = -1 
 ...




@dataclass
class opus_metadata_bsf(): # opus_metadata_bsf
 gain:int = 0 
 ...




@dataclass
class pcm_rechunk_bsf(): # pcm_rechunk_bsf
 nb_out_samples:int = 1024
 n:int = 1024
 pad:bool = True
 p:bool = True
 frame_rate:float|str = '0/1'
 r:float|str = '0/1' 
 ...


PRORES_METADATA_BSF_COLOR_PRIMARIES = Literal['auto', 'unknown', 'bt709', 'bt470bg', 'smpte170m', 'bt2020', 'smpte431', 'smpte432']
PRORES_METADATA_BSF_COLOR_TRC = Literal['auto', 'unknown', 'bt709', 'smpte2084', 'arib-std-b67']
PRORES_METADATA_BSF_COLORSPACE = Literal['auto', 'unknown', 'bt709', 'smpte170m', 'bt2020nc']

@dataclass
class prores_metadata_bsf(): # prores_metadata_bsf
 color_primaries:PRORES_METADATA_BSF_COLOR_PRIMARIES = 'auto'
 color_trc:PRORES_METADATA_BSF_COLOR_TRC = 'auto'
 colorspace:PRORES_METADATA_BSF_COLORSPACE = 'auto' 
 ...


REMOVE_EXTRADATA_FREQ = Literal['k', 'keyframe', 'e', 'all']

@dataclass
class remove_extradata(): # remove_extradata
 freq:REMOVE_EXTRADATA_FREQ = 'keyframe' 
 ...




@dataclass
class setts_bsf(): # setts_bsf
 ts:str = "TS"
 pts:str = None
 dts:str = None
 duration:str = "DURATION"
 time_base:float|str = '0/1' 
 ...


VP9_METADATA_BSF_COLOR_SPACE = Literal['unknown', 'bt601', 'bt709', 'smpte170', 'smpte240', 'bt2020', 'rgb']
VP9_METADATA_BSF_COLOR_RANGE = Literal['tv', 'pc']

@dataclass
class vp9_metadata_bsf(): # vp9_metadata_bsf
 color_space:VP9_METADATA_BSF_COLOR_SPACE = '-1'
 color_range:VP9_METADATA_BSF_COLOR_RANGE = '-1' 
 ...


