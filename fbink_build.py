#!/usr/bin/env python2
#
# out-of-line, API mode Python FFI bindings for FBink, via cffi
#
# c.f., https://cffi.readthedocs.io/en/latest/overview.html
#
##

from cffi import FFI
ffibuilder = FFI()

# cdef() expects a string listing the C types, functions and
# globals needed from Python. The string follows the C syntax.
# NOTE: We re-purpose the Lua cdefs generated via ffi-cdecl
ffibuilder.cdef("""
static const int FBFD_AUTO = -1;
static const int LAST_MARKER = 0;
typedef enum {
  IBM = 0,
  UNSCII = 1,
  UNSCII_ALT = 2,
  UNSCII_THIN = 3,
  UNSCII_FANTASY = 4,
  UNSCII_MCR = 5,
  UNSCII_TALL = 6,
  BLOCK = 7,
  LEGGIE = 8,
  VEGGIE = 9,
  KATES = 10,
  FKP = 11,
  CTRLD = 12,
  ORP = 13,
  ORPB = 14,
  ORPI = 15,
  SCIENTIFICA = 16,
  SCIENTIFICAB = 17,
  SCIENTIFICAI = 18,
  TERMINUS = 19,
  TERMINUSB = 20,
  FATTY = 21,
  SPLEEN = 22,
  TEWI = 23,
  TEWIB = 24,
  TOPAZ = 25,
  MICROKNIGHT = 26,
  VGA = 27,
  UNIFONT = 28,
  UNIFONTDW = 29,
  COZETTE = 30,
  FONT_MAX = 255,
} FONT_INDEX_E;
typedef unsigned char FONT_INDEX_T;
typedef enum {
  FNT_REGULAR = 0,
  FNT_ITALIC = 1,
  FNT_BOLD = 2,
  FNT_BOLD_ITALIC = 3,
} FONT_STYLE_E;
typedef int FONT_STYLE_T;
typedef enum {
  NONE = 0,
  CENTER = 1,
  EDGE = 2,
  ALIGN_MAX = 255,
} ALIGN_INDEX_E;
typedef unsigned char ALIGN_INDEX_T;
typedef enum {
  NO_PADDING = 0,
  HORI_PADDING = 1,
  VERT_PADDING = 2,
  FULL_PADDING = 3,
  MAX_PADDING = 255,
} PADDING_INDEX_E;
typedef unsigned char PADDING_INDEX_T;
typedef enum {
  FG_BLACK = 0,
  FG_GRAY1 = 1,
  FG_GRAY2 = 2,
  FG_GRAY3 = 3,
  FG_GRAY4 = 4,
  FG_GRAY5 = 5,
  FG_GRAY6 = 6,
  FG_GRAY7 = 7,
  FG_GRAY8 = 8,
  FG_GRAY9 = 9,
  FG_GRAYA = 10,
  FG_GRAYB = 11,
  FG_GRAYC = 12,
  FG_GRAYD = 13,
  FG_GRAYE = 14,
  FG_WHITE = 15,
  FG_MAX = 255,
} FG_COLOR_INDEX_E;
typedef unsigned char FG_COLOR_INDEX_T;
typedef enum {
  BG_WHITE = 0,
  BG_GRAYE = 1,
  BG_GRAYD = 2,
  BG_GRAYC = 3,
  BG_GRAYB = 4,
  BG_GRAYA = 5,
  BG_GRAY9 = 6,
  BG_GRAY8 = 7,
  BG_GRAY7 = 8,
  BG_GRAY6 = 9,
  BG_GRAY5 = 10,
  BG_GRAY4 = 11,
  BG_GRAY3 = 12,
  BG_GRAY2 = 13,
  BG_GRAY1 = 14,
  BG_BLACK = 15,
  BG_MAX = 255,
} BG_COLOR_INDEX_E;
typedef unsigned char BG_COLOR_INDEX_T;
typedef enum {
  WFM_AUTO = 0,
  WFM_DU = 1,
  WFM_GC16 = 2,
  WFM_GC4 = 3,
  WFM_A2 = 4,
  WFM_GL16 = 5,
  WFM_REAGL = 6,
  WFM_REAGLD = 7,
  WFM_GC16_FAST = 8,
  WFM_GL16_FAST = 9,
  WFM_DU4 = 10,
  WFM_GL4 = 11,
  WFM_GL16_INV = 12,
  WFM_GCK16 = 13,
  WFM_GLKW16 = 14,
  WFM_INIT = 15,
  WFM_UNKNOWN = 16,
  WFM_INIT2 = 17,
  WFM_MAX = 255,
} WFM_MODE_INDEX_E;
typedef unsigned char WFM_MODE_INDEX_T;
typedef enum {
  HWD_PASSTHROUGH = 0,
  HWD_FLOYD_STEINBERG = 1,
  HWD_ATKINSON = 2,
  HWD_ORDERED = 3,
  HWD_QUANT_ONLY = 4,
  HWD_LEGACY = 255,
} HW_DITHER_INDEX_E;
typedef unsigned char HW_DITHER_INDEX_T;
typedef enum {
  NTX_ROTA_STRAIGHT = 0,
  NTX_ROTA_ALL_INVERTED = 1,
  NTX_ROTA_ODD_INVERTED = 2,
  NTX_ROTA_SANE = 3,
  NTX_ROTA_MAX = 255,
} NTX_ROTA_INDEX_E;
typedef unsigned char NTX_ROTA_INDEX_T;
typedef struct {
  long int user_hz;
  const char *restrict font_name;
  uint32_t view_width;
  uint32_t view_height;
  uint32_t screen_width;
  uint32_t screen_height;
  uint32_t bpp;
  char device_name[16];
  char device_codename[16];
  char device_platform[16];
  short unsigned int device_id;
  uint8_t pen_fg_color;
  uint8_t pen_bg_color;
  short unsigned int screen_dpi;
  short unsigned int font_w;
  short unsigned int font_h;
  short unsigned int max_cols;
  short unsigned int max_rows;
  uint8_t view_hori_origin;
  uint8_t view_vert_origin;
  uint8_t view_vert_offset;
  uint8_t fontsize_mult;
  uint8_t glyph_width;
  uint8_t glyph_height;
  bool is_perfect_fit;
  bool is_kobo_non_mt;
  uint8_t ntx_boot_rota;
  NTX_ROTA_INDEX_T ntx_rota_quirk;
  bool is_ntx_quirky_landscape;
  uint8_t current_rota;
  bool can_rotate;
} FBInkState;
typedef struct {
  short int row;
  short int col;
  uint8_t fontmult;
  FONT_INDEX_T fontname;
  bool is_inverted;
  bool is_flashing;
  bool is_cleared;
  bool is_centered;
  short int hoffset;
  short int voffset;
  bool is_halfway;
  bool is_padded;
  bool is_rpadded;
  FG_COLOR_INDEX_T fg_color;
  BG_COLOR_INDEX_T bg_color;
  bool is_overlay;
  bool is_bgless;
  bool is_fgless;
  bool no_viewport;
  bool is_verbose;
  bool is_quiet;
  bool ignore_alpha;
  ALIGN_INDEX_T halign;
  ALIGN_INDEX_T valign;
  short int scaled_width;
  short int scaled_height;
  WFM_MODE_INDEX_T wfm_mode;
  HW_DITHER_INDEX_T dithering_mode;
  bool sw_dithering;
  bool is_nightmode;
  bool no_refresh;
  bool to_syslog;
} FBInkConfig;
typedef struct {
  struct {
    void *regular;
    void *italic;
    void *bold;
    void *bold_italic;
  } font;
  struct {
    short int top;
    short int bottom;
    short int left;
    short int right;
  } margins;
  FONT_STYLE_T style;
  float size_pt;
  short unsigned int size_px;
  bool is_centered;
  PADDING_INDEX_T padding;
  bool is_formatted;
  bool compute_only;
  bool no_truncation;
} FBInkOTConfig;
typedef struct {
  short unsigned int computed_lines;
  short unsigned int rendered_lines;
  bool truncated;
} FBInkOTFit;
typedef struct {
  short unsigned int left;
  short unsigned int top;
  short unsigned int width;
  short unsigned int height;
} FBInkRect;
typedef struct {
  unsigned char *restrict data;
  size_t stride;
  size_t size;
  FBInkRect area;
  FBInkRect clip;
  uint8_t rota;
  uint8_t bpp;
  bool is_full;
} FBInkDump;
const char *fbink_version(void);
int fbink_open(void);
int fbink_close(int);
int fbink_init(int, const FBInkConfig *restrict);
void fbink_state_dump(const FBInkConfig *restrict);
void fbink_get_state(const FBInkConfig *restrict, FBInkState *restrict);
int fbink_print(int, const char *restrict, const FBInkConfig *restrict);
int fbink_add_ot_font(const char *, FONT_STYLE_T);
int fbink_add_ot_font_v2(const char *, FONT_STYLE_T, FBInkOTConfig *restrict);
int fbink_free_ot_fonts(void);
int fbink_free_ot_fonts_v2(FBInkOTConfig *restrict);
int fbink_print_ot(int, const char *restrict, const FBInkOTConfig *restrict, const FBInkConfig *restrict, FBInkOTFit *restrict);
int fbink_printf(int, const FBInkOTConfig *restrict, const FBInkConfig *restrict, const char *, ...);
int fbink_refresh(int, uint32_t, uint32_t, uint32_t, uint32_t, const FBInkConfig *restrict);
int fbink_wait_for_submission(int, uint32_t);
int fbink_wait_for_complete(int, uint32_t);
uint32_t fbink_get_last_marker(void);
static const int OK_BPP_CHANGE = 512;
static const int OK_ROTA_CHANGE = 1024;
static const int OK_LAYOUT_CHANGE = 2048;
int fbink_reinit(int, const FBInkConfig *restrict);
void fbink_update_verbosity(const FBInkConfig *restrict);
int fbink_update_pen_colors(const FBInkConfig *restrict);
static const int OK_ALREADY_SAME = 512;
int fbink_set_fg_pen_gray(uint8_t, bool, bool);
int fbink_set_bg_pen_gray(uint8_t, bool, bool);
int fbink_set_fg_pen_rgba(uint8_t, uint8_t, uint8_t, uint8_t, bool, bool);
int fbink_set_bg_pen_rgba(uint8_t, uint8_t, uint8_t, uint8_t, bool, bool);
int fbink_print_progress_bar(int, uint8_t, const FBInkConfig *restrict);
int fbink_print_activity_bar(int, uint8_t, const FBInkConfig *restrict);
int fbink_print_image(int, const char *, short int, short int, const FBInkConfig *restrict);
int fbink_print_raw_data(int, unsigned char *, const int, const int, const size_t, short int, short int, const FBInkConfig *restrict);
int fbink_cls(int, const FBInkConfig *restrict, const FBInkRect *restrict);
int fbink_grid_clear(int, short unsigned int, short unsigned int, const FBInkConfig *restrict);
int fbink_grid_refresh(int, short unsigned int, short unsigned int, const FBInkConfig *restrict);
int fbink_dump(int, FBInkDump *restrict);
int fbink_region_dump(int, short int, short int, short unsigned int, short unsigned int, const FBInkConfig *restrict, FBInkDump *restrict);
int fbink_restore(int, const FBInkConfig *restrict, const FBInkDump *restrict);
int fbink_free_dump_data(FBInkDump *restrict);
FBInkRect fbink_get_last_rect(void);
int fbink_button_scan(int, bool, bool);
int fbink_wait_for_usbms_processing(int, bool);
""")

# This describes the extension module "_fbink" to produce.
ffibuilder.set_source("_fbink",
"""
     #include "fbink.h"   // the C header of the library
""",
     libraries=['fbink'])   # library name, for the linker

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
