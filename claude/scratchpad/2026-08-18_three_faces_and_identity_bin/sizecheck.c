#include <stdio.h>
#include <stddef.h>
#include "monad_identity.h"
int main(void){
    printf("mi_header_t %zu\n", sizeof(mi_header_t));
    printf("mi_entry_t %zu\n",  sizeof(mi_entry_t));
    printf("mi_chan_t %zu\n",   sizeof(mi_chan_t));
    printf("mi_edge_t %zu\n",   sizeof(mi_edge_t));
    printf("off.spell %zu\n",   offsetof(mi_entry_t, spell));
    printf("off.chan_off %zu\n",offsetof(mi_entry_t, chan_off));
    printf("off.addr_fp %zu\n", offsetof(mi_entry_t, addr_fp));
    printf("off.parent %zu\n",  offsetof(mi_entry_t, parent));
    printf("hdr.s_entries %zu\n", offsetof(mi_header_t, s_entries));
    printf("hdr.checksum %zu\n",  offsetof(mi_header_t, checksum));
    return 0;
}
