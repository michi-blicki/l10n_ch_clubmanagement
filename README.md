# l10n_ch_clubmanagement

Swiss localization addon for Odoo Club Management system.

## Overview

This addon extends the Odoo Club Management module with Switzerland-specific features for sports associations and clubs. It provides Swiss-compliant member registration, particularly for youth sports programs requiring J+S (Jugend+Sport) certification.

## Features

- **J+S Number Field**: Add and manage J+S numbers for club members (required for Swiss youth sports activities)
- **Minor Member Validation**: Automatic enforcement of Swiss Social Insurance Number (SSNID) requirement for members below the age of majority
- **Age-based Classification**: Automatic member classification based on configurable age thresholds (default: 18 years)
- **Data Integrity**: Prevents registration of minors without proper identification compliance

## Requirements

- Odoo 18.0 Community Edition or later
- **clubmanagement** addon (https://github.com/michi-blicki/Odoo_Clubmanagement)

## Installation

1. Clone or download this addon into your Odoo addons directory
2. Ensure the `clubmanagement` addon is installed
3. Activate the addon in your Odoo instance

## Configuration

The addon uses the following configurable parameters:
- `clubmanagement.age_of_majority` (default: 18) - Age threshold for minor member validation

## License

AGPL-3

## Support

This addon is developed and maintained for Swiss club management use cases. Community contributions and issue reports are welcome.

For issues, feature requests, or contributions, please visit: https://github.com/michi-blicki/l10n_ch_clubmanagement

## Author

Michael Blickenstorfer

---

**Made with ❤️ for the Swiss Odoo Community**