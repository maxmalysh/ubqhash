#pragma once

#include "compiler.h"
#include <stdint.h>
#include <stdlib.h>

#ifdef __cplusplus
extern "C" {
#endif

struct ubqhash_h256;

void BLAKE2S_256(struct ubqhash_h256 const* ret, uint8_t const* data, size_t size);

#ifdef __cplusplus
}
#endif
