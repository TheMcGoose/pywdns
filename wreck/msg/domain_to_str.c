#include "private.h"

/**
 * Convert a domain name to a human-readable string.
 *
 * \param[in] src domain name in wire format
 * \param[out] dst caller-allocated string buffer
 * 
 * \return Number of bytes read from src.
 */

size_t
wreck_domain_to_str(const uint8_t *src, char *dst)
{
	size_t bytes_read = 0;
	uint8_t oclen;

	oclen = *src;
	while (oclen != 0) {
		src++;

		bytes_read += oclen + 1 /* length octet */;

		while (oclen--)
			*dst++ = *src++;
		*dst++ = '.';
		oclen = *src;
	}

	*dst = '\0';
	return (bytes_read);
}