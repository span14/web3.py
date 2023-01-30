from eth_utils.curried import (
  to_checksum_address,
  is_address
)
from eth_utils.conversions import hexstr_if_str, to_hex
from eth_utils.types import is_text

from eth_typing import Address, AnyAddress, ChecksumAddress, HexAddress, HexStr
from typing import Any, AnyStr

def is_xdc_prefixed(value: Any) -> bool:
  if not is_text(value):
    raise TypeError(
      "is_xdc_prefixed requires text typed arguments. Got: {0}".format(repr(value))
    )
  return value.startswith("xdc") or value.startswith("XDC")

def is_xdc_address(value: Any) -> bool:
  if value is None:
    return False
  text = remove_xdc_prefix(value) if is_xdc_prefixed(value) else value
  return is_address(text)

def remove_xdc_prefix(value: HexStr) -> HexStr:
  if is_xdc_prefixed(value):
    return HexStr(value[3:])
  return value

def to_xdc_checksum_address(value: AnyStr) -> ChecksumAddress:
  text = remove_xdc_prefix(value) if is_xdc_prefixed(value) else value
  try:
    hex_address = hexstr_if_str(to_hex, text).lower()
  except AttributeError:
    raise TypeError(
      "Value must be any string, instead got type {}".format(type(value))
    )
  return to_checksum_address(hex_address)
    

