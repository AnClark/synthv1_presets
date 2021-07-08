import os
import base64
import binascii
import re
import sys
import argparse
import xml.dom.minidom as minidom

XML_TEMPLATE_SYNTHV1 = """<!DOCTYPE synthv1>
<preset name="{NAME}" version="0.9.22.32git.e83414.dirty [develop]">
 <params>
  <param index="0" name="DCO1_SHAPE1">{DCO1_SHAPE1}</param>
  <param index="1" name="DCO1_WIDTH1">{DCO1_WIDTH1}</param>
  <param index="2" name="DCO1_BANDL1">{DCO1_BANDL1}</param>
  <param index="3" name="DCO1_SYNC1">{DCO1_SYNC1}</param>
  <param index="4" name="DCO1_SHAPE2">{DCO1_SHAPE2}</param>
  <param index="5" name="DCO1_WIDTH2">{DCO1_WIDTH2}</param>
  <param index="6" name="DCO1_BANDL2">{DCO1_BANDL2}</param>
  <param index="7" name="DCO1_SYNC2">{DCO1_SYNC2}</param>
  <param index="8" name="DCO1_BALANCE">{DCO1_BALANCE}</param>
  <param index="9" name="DCO1_DETUNE">{DCO1_DETUNE}</param>
  <param index="10" name="DCO1_PHASE">{DCO1_PHASE}</param>
  <param index="11" name="DCO1_RINGMOD">{DCO1_RINGMOD}</param>
  <param index="12" name="DCO1_OCTAVE">{DCO1_OCTAVE}</param>
  <param index="13" name="DCO1_TUNING">{DCO1_TUNING}</param>
  <param index="14" name="DCO1_GLIDE">{DCO1_GLIDE}</param>
  <param index="15" name="DCO1_ENVTIME">{DCO1_ENVTIME}</param>
  <param index="16" name="DCF1_ENABLED">{DCF1_ENABLED}</param>
  <param index="17" name="DCF1_CUTOFF">{DCF1_CUTOFF}</param>
  <param index="18" name="DCF1_RESO">{DCF1_RESO}</param>
  <param index="19" name="DCF1_TYPE">{DCF1_TYPE}</param>
  <param index="20" name="DCF1_SLOPE">{DCF1_SLOPE}</param>
  <param index="21" name="DCF1_ENVELOPE">{DCF1_ENVELOPE}</param>
  <param index="22" name="DCF1_ATTACK">{DCF1_ATTACK}</param>
  <param index="23" name="DCF1_DECAY">{DCF1_DECAY}</param>
  <param index="24" name="DCF1_SUSTAIN">{DCF1_SUSTAIN}</param>
  <param index="25" name="DCF1_RELEASE">{DCF1_RELEASE}</param>
  <param index="26" name="LFO1_ENABLED">{LFO1_ENABLED}</param>
  <param index="27" name="LFO1_SHAPE">{LFO1_SHAPE}</param>
  <param index="28" name="LFO1_WIDTH">{LFO1_WIDTH}</param>
  <param index="29" name="LFO1_BPM">{LFO1_BPM}</param>
  <param index="30" name="LFO1_RATE">{LFO1_RATE}</param>
  <param index="31" name="LFO1_SYNC">{LFO1_SYNC}</param>
  <param index="32" name="LFO1_SWEEP">{LFO1_SWEEP}</param>
  <param index="33" name="LFO1_PITCH">{LFO1_PITCH}</param>
  <param index="34" name="LFO1_BALANCE">{LFO1_BALANCE}</param>
  <param index="35" name="LFO1_RINGMOD">{LFO1_RINGMOD}</param>
  <param index="36" name="LFO1_CUTOFF">{LFO1_CUTOFF}</param>
  <param index="37" name="LFO1_RESO">{LFO1_RESO}</param>
  <param index="38" name="LFO1_PANNING">{LFO1_PANNING}</param>
  <param index="39" name="LFO1_VOLUME">{LFO1_VOLUME}</param>
  <param index="40" name="LFO1_ATTACK">{LFO1_ATTACK}</param>
  <param index="41" name="LFO1_DECAY">{LFO1_DECAY}</param>
  <param index="42" name="LFO1_SUSTAIN">{LFO1_SUSTAIN}</param>
  <param index="43" name="LFO1_RELEASE">{LFO1_RELEASE}</param>
  <param index="44" name="DCA1_VOLUME">{DCA1_VOLUME}</param>
  <param index="45" name="DCA1_ATTACK">{DCA1_ATTACK}</param>
  <param index="46" name="DCA1_DECAY">{DCA1_DECAY}</param>
  <param index="47" name="DCA1_SUSTAIN">{DCA1_SUSTAIN}</param>
  <param index="48" name="DCA1_RELEASE">{DCA1_RELEASE}</param>
  <param index="49" name="OUT1_WIDTH">{OUT1_WIDTH}</param>
  <param index="50" name="OUT1_PANNING">{OUT1_PANNING}</param>
  <param index="51" name="OUT1_FXSEND">{OUT1_FXSEND}</param>
  <param index="52" name="OUT1_VOLUME">{OUT1_VOLUME}</param>
  <param index="53" name="DEF1_PITCHBEND">{DEF1_PITCHBEND}</param>
  <param index="54" name="DEF1_MODWHEEL">{DEF1_MODWHEEL}</param>
  <param index="55" name="DEF1_PRESSURE">{DEF1_PRESSURE}</param>
  <param index="56" name="DEF1_VELOCITY">{DEF1_VELOCITY}</param>
  <param index="57" name="DEF1_CHANNEL">{DEF1_CHANNEL}</param>
  <param index="58" name="DEF1_MONO">{DEF1_MONO}</param>
  <param index="59" name="DCO2_SHAPE1">{DCO2_SHAPE1}</param>
  <param index="60" name="DCO2_WIDTH1">{DCO2_WIDTH1}</param>
  <param index="61" name="DCO2_BANDL1">{DCO2_BANDL1}</param>
  <param index="62" name="DCO2_SYNC1">{DCO2_SYNC1}</param>
  <param index="63" name="DCO2_SHAPE2">{DCO2_SHAPE2}</param>
  <param index="64" name="DCO2_WIDTH2">{DCO2_WIDTH2}</param>
  <param index="65" name="DCO2_BANDL2">{DCO2_BANDL2}</param>
  <param index="66" name="DCO2_SYNC2">{DCO2_SYNC2}</param>
  <param index="67" name="DCO2_BALANCE">{DCO2_BALANCE}</param>
  <param index="68" name="DCO2_DETUNE">{DCO2_DETUNE}</param>
  <param index="69" name="DCO2_PHASE">{DCO2_PHASE}</param>
  <param index="70" name="DCO2_RINGMOD">{DCO2_RINGMOD}</param>
  <param index="71" name="DCO2_OCTAVE">{DCO2_OCTAVE}</param>
  <param index="72" name="DCO2_TUNING">{DCO2_TUNING}</param>
  <param index="73" name="DCO2_GLIDE">{DCO2_GLIDE}</param>
  <param index="74" name="DCO2_ENVTIME">{DCO2_ENVTIME}</param>
  <param index="75" name="DCF2_ENABLED">{DCF2_ENABLED}</param>
  <param index="76" name="DCF2_CUTOFF">{DCF2_CUTOFF}</param>
  <param index="77" name="DCF2_RESO">{DCF2_RESO}</param>
  <param index="78" name="DCF2_TYPE">{DCF2_TYPE}</param>
  <param index="79" name="DCF2_SLOPE">{DCF2_SLOPE}</param>
  <param index="80" name="DCF2_ENVELOPE">{DCF2_ENVELOPE}</param>
  <param index="81" name="DCF2_ATTACK">{DCF2_ATTACK}</param>
  <param index="82" name="DCF2_DECAY">{DCF2_DECAY}</param>
  <param index="83" name="DCF2_SUSTAIN">{DCF2_SUSTAIN}</param>
  <param index="84" name="DCF2_RELEASE">{DCF2_RELEASE}</param>
  <param index="85" name="LFO2_ENABLED">{LFO2_ENABLED}</param>
  <param index="86" name="LFO2_SHAPE">{LFO2_SHAPE}</param>
  <param index="87" name="LFO2_WIDTH">{LFO2_WIDTH}</param>
  <param index="88" name="LFO2_BPM">{LFO2_BPM}</param>
  <param index="89" name="LFO2_RATE">{LFO2_RATE}</param>
  <param index="90" name="LFO2_SYNC">{LFO2_SYNC}</param>
  <param index="91" name="LFO2_SWEEP">{LFO2_SWEEP}</param>
  <param index="92" name="LFO2_PITCH">{LFO2_PITCH}</param>
  <param index="93" name="LFO2_BALANCE">{LFO2_BALANCE}</param>
  <param index="94" name="LFO2_RINGMOD">{LFO2_RINGMOD}</param>
  <param index="95" name="LFO2_CUTOFF">{LFO2_CUTOFF}</param>
  <param index="96" name="LFO2_RESO">{LFO2_RESO}</param>
  <param index="97" name="LFO2_PANNING">{LFO2_PANNING}</param>
  <param index="98" name="LFO2_VOLUME">{LFO2_VOLUME}</param>
  <param index="99" name="LFO2_ATTACK">{LFO2_ATTACK}</param>
  <param index="100" name="LFO2_DECAY">{LFO2_DECAY}</param>
  <param index="101" name="LFO2_SUSTAIN">{LFO2_SUSTAIN}</param>
  <param index="102" name="LFO2_RELEASE">{LFO2_RELEASE}</param>
  <param index="103" name="DCA2_VOLUME">{DCA2_VOLUME}</param>
  <param index="104" name="DCA2_ATTACK">{DCA2_ATTACK}</param>
  <param index="105" name="DCA2_DECAY">{DCA2_DECAY}</param>
  <param index="106" name="DCA2_SUSTAIN">{DCA2_SUSTAIN}</param>
  <param index="107" name="DCA2_RELEASE">{DCA2_RELEASE}</param>
  <param index="108" name="OUT2_WIDTH">{OUT2_WIDTH}</param>
  <param index="109" name="OUT2_PANNING">{OUT2_PANNING}</param>
  <param index="110" name="OUT2_FXSEND">{OUT2_FXSEND}</param>
  <param index="111" name="OUT2_VOLUME">{OUT2_VOLUME}</param>
  <param index="112" name="DEF2_PITCHBEND">{DEF2_PITCHBEND}</param>
  <param index="113" name="DEF2_MODWHEEL">{DEF2_MODWHEEL}</param>
  <param index="114" name="DEF2_PRESSURE">{DEF2_PRESSURE}</param>
  <param index="115" name="DEF2_VELOCITY">{DEF2_VELOCITY}</param>
  <param index="116" name="DEF2_CHANNEL">{DEF2_CHANNEL}</param>
  <param index="117" name="DEF2_MONO">{DEF2_MONO}</param>
  <param index="118" name="CHO1_WET">{CHO1_WET}</param>
  <param index="119" name="CHO1_DELAY">{CHO1_DELAY}</param>
  <param index="120" name="CHO1_FEEDB">{CHO1_FEEDB}</param>
  <param index="121" name="CHO1_RATE">{CHO1_RATE}</param>
  <param index="122" name="CHO1_MOD">{CHO1_MOD}</param>
  <param index="123" name="FLA1_WET">{FLA1_WET}</param>
  <param index="124" name="FLA1_DELAY">{FLA1_DELAY}</param>
  <param index="125" name="FLA1_FEEDB">{FLA1_FEEDB}</param>
  <param index="126" name="FLA1_DAFT">{FLA1_DAFT}</param>
  <param index="127" name="PHA1_WET">{PHA1_WET}</param>
  <param index="128" name="PHA1_RATE">{PHA1_RATE}</param>
  <param index="129" name="PHA1_FEEDB">{PHA1_FEEDB}</param>
  <param index="130" name="PHA1_DEPTH">{PHA1_DEPTH}</param>
  <param index="131" name="PHA1_DAFT">{PHA1_DAFT}</param>
  <param index="132" name="DEL1_WET">{DEL1_WET}</param>
  <param index="133" name="DEL1_DELAY">{DEL1_DELAY}</param>
  <param index="134" name="DEL1_FEEDB">{DEL1_FEEDB}</param>
  <param index="135" name="DEL1_BPM">{DEL1_BPM}</param>
  <param index="136" name="REV1_WET">{REV1_WET}</param>
  <param index="137" name="REV1_ROOM">{REV1_ROOM}</param>
  <param index="138" name="REV1_DAMP">{REV1_DAMP}</param>
  <param index="139" name="REV1_FEEDB">{REV1_FEEDB}</param>
  <param index="140" name="REV1_WIDTH">{REV1_WIDTH}</param>
  <param index="141" name="DYN1_COMPRESS">{DYN1_COMPRESS}</param>
  <param index="142" name="DYN1_LIMITER">{DYN1_LIMITER}</param>
  <param index="143" name="KEY1_LOW">{KEY1_LOW}</param>
  <param index="144" name="KEY1_HIGH">{KEY1_HIGH}</param>
 </params>
</preset>
"""


class Logger():
    def info(self, message):
        print("[INFO] {msg}".format(msg=message))

    def error(self, message, exit_number):
        print("[ERROR] {msg}".format(msg=message))
        sys.exit(exit_number)

    def warning(self, message):
        print("[WARNING] {msg}".format(msg=message))


def read_rpl(rpl_filename):
    # Store raw preset data (preset_name:preset_data)
    # "Preset data" is a roughly arrayed string, using \x00 as separator sparsely.
    # Example: "DCO1_SHAPE1 0.100 DCO1_WIDTH1 1.500\x00"
    preset_list = {}

    # Open RPL file, then extract preset name and Base64-decoded content
    try:
        rpl_content = open(rpl_filename, "rb").read().decode("utf-8")
    except FileNotFoundError as err:
        Logger().error(message="Cannot find RPL file '{filename}'".format(
            filename=rpl_filename), exit_number=1)

    except Exception as err:
        Logger().error(message="Cannot read RPL file '{filename}'\n\t{err_message}".format(
            filename=rpl_filename, err_message=err.args[0]), exit_number=16)

    raw_preset_list = re.findall(
        r"<PRESET\s+`(.*)`([\w=+\s]+)>", rpl_content, re.M)

    if len(raw_preset_list) <= 0:
        Logger().error("Cannot detect any presets.", exit_number=5)

    # Decode all preset contents
    for preset in raw_preset_list:
        raw_preset_base64 = preset[1].replace(" ", "")

        try:
            preset_data = base64.b64decode(raw_preset_base64).decode("utf-8")
        except binascii.Error as base64_error:         # Base64 parse error
            Logger().error(message="Base64 decode error at preset '{preset_name}' ({message})\n\tYour RPL file may have corrupted!".format(preset_name=preset[0],
                                                                                                                                           message=base64_error.args[0]), exit_number=2)

        # Consider if user omitted preset name
        if preset[0].strip() == "":
            fallback_preset_name = "unknown_{hash}".format(
                hash=str(hash(preset_data)))
            Logger().warning(message="Empty preset name found. Renaming as {new_name}".format(
                new_name=fallback_preset_name))

            preset_list[fallback_preset_name] = preset_data
        else:
            preset_list[preset[0]] = preset_data

    return preset_list


def check_rpl_type(rpl_filename):
    # Open RPL file
    try:
        rpl_content = open(rpl_filename, "rb").read().decode("utf-8")
    except FileNotFoundError as err:
        Logger().error(message="Cannot find RPL file '{filename}'".format(
            filename=rpl_filename), exit_number=1)

    except Exception as err:
        Logger().error(message="Cannot read RPL file '{filename}'\n\t{err_message}".format(
            filename=rpl_filename, err_message=err.args[0]), exit_number=16)

    preset_name_result = re.findall(
        r'<REAPER_PRESET_LIBRARY\s+"([^"]+)"', rpl_content)
    if not preset_name_result:
        Logger().error("Cannot detect preset type. Manually specify with -t if needed.", exit_number=9)

    if re.search(r"synthv1", preset_name_result[0], re.I):
        Logger().info("Detected SynthV1 preset")
        return "SynthV1"
    elif re.search(r"padthv1", preset_name_result[0], re.I):
        Logger().info("Detected PadthV1 preset")
        return "PadthV1"
    else:
        Logger().warning("Unknown preset type. Assume SynthV1.")
        return "SynthV1"


def preset_list_to_xml(preset_list, type="SynthV1"):
    # Store generated preset XML content (preset_name:XML_content)
    preset_xml_collection = {}

    # Parse preset data into a dictionary.
    def parse_preset_data(preset_data):
        preset_content_dict = {}

        parsed_preset_data = re.findall(r"([\w_]+)\s([\d\.\-]+)", preset_data)

        for entry in parsed_preset_data:
            preset_content_dict[entry[0]] = entry[1]

        return preset_content_dict

    # Render XML template.
    def render_template(name, **preset_content_dict):
        # Remove quotation marks, or Qt won't recognize my XML file
        if re.search(r'"', name):
            Logger().warning(message="Omitting this preset name's quotation marks ↓\n\t{preset_name}".format(
                preset_name=name))
            name = name.replace('"', '')

        try:
            return XML_TEMPLATE_SYNTHV1.format(**preset_content_dict, NAME=name)
        except KeyError as key_err:
            Logger().error(message="ERROR: Insufficient preset data detected.\n\tOn preset: '{preset_name}'\n\tPreset entry: '{entry}'\nMake sure this is {type}'s RPL file.".format(
                preset_name=name, entry=key_err.args[0], type=type), exit_number=3)

    # Extract and process state XML (for PadthV1)
    # All states (including params and samples) are stored in a full XML file,
    # which is directly encoded into the preset storage.
    def extract_padthv1_state(preset_data, name=""):
        RE_STATE_SELECTOR = re.compile(r"<STATE\x00<X.+?\x00(.*?)\x00>", re.M)

        # Check if it's PadthV1's bank file
        if not RE_STATE_SELECTOR.search(preset_data):
            Logger().error("Not a PadthV1 REAPER user bank file.", exit_number=7)

        # Parse states (including sample data)
        extracted_raw_state_base64 = RE_STATE_SELECTOR.findall(
            preset_data, re.M)

        try:
            preset_state_xml = base64.b64decode(
                extracted_raw_state_base64[0]).decode("utf-8")
        except binascii.Error as base64_error:         # Base64 parse error
            Logger().error(message="Base64 decode error when parsing preset STATE for '{preset_name}' ({message})\n\tYour RPL file may have corrupted!".format(preset_name=name,
                                                                                                                                                               message=base64_error.args[0]), exit_number=2)

        # Write some metadata via DOM processor
        doc = minidom.parseString(preset_state_xml)
        doc.getElementsByTagName("state")[0].setAttribute("name", name)

        return doc.toxml().replace("state", "preset")       # Remember to replace tag name

    # Convert all preset data into XML, storing them into a dictionary
    if type.lower() == "padthv1":       # For PadthV1
        for p in preset_list.keys():
            preset_xml_collection[p] = extract_padthv1_state(
                name=p, preset_data=preset_list[p])
    else:           # For other Vee-One products
        for p in preset_list.keys():
            current_preset_content = parse_preset_data(preset_list[p])
            preset_xml_collection[p] = render_template(
                name=p, **current_preset_content)

    return preset_xml_collection


def rpl_to_xml(rpl_filename, target_path, overwrite_all=False, type="auto"):
    # Filter out illeagal filename characters
    def preprocess_filename(filename):
        if re.search(r'[\\"]', filename):
            filename = filename.replace('\\', '').replace('"', '')

        return filename

    # Auto determine RPL type if needed
    type_assume_mode = ""
    if type == "auto" or type.strip() == "":
        type = check_rpl_type(rpl_filename)
        type_assume_mode = "(auto detect)"
    else:
        type_assume_mode = "(manually assume)"

    Logger().info("Processing REAPER user preset bank for Vee-One Suite\n\tType: {type} {type_assume_mode}\n\tFile Name: {filename}".format(
        type=type, filename=rpl_filename, type_assume_mode=type_assume_mode))

    # Parse and convert RPL file internally
    preset_list = read_rpl(rpl_filename)
    preset_xml_collection = preset_list_to_xml(preset_list, type=type)

    # Logger().info("Got preset count: {preset_count}".format(
    #    preset_count=len(preset_xml_collection.keys())))

    # Create target directory if not exist
    try:
        if not os.path.exists(target_path):
            os.mkdir(target_path)
    except Exception as err:
        Logger().error(message="Cannot create target directory: {err_message}".format(
            err_message=err.args[1]), exit_number=16)

    # Clean target directory if needed (usually for distribution)
    if overwrite_all:
        try:
            for f in os.listdir(target_path):
                os.remove("{target}/{name}".format(target=target_path, name=f))
        except Exception as err:
            Logger().error(message="Error while clearing target directory: {err_message}".format(
                err_message=err.args[1]), exit_number=16)

    # Save XML preset files into specified directory
    converted_count = 0
    for p in preset_xml_collection.keys():
        try:
            open("{target}/{name}.{type}".format(target=target_path, type=type.lower(),
                                                 name=preprocess_filename(p)), "w").write(preset_xml_collection[p])
            converted_count += 1
        except Exception as err:
            Logger().error(message="Cannot write preset '{preset_name}': {err_message}".format(preset_name=preprocess_filename(p),
                                                                                               err_message=err.args[1]), exit_number=16)

    Logger().info("Summary:\n\tPreset count:     {preset_count}\n\tConverted count:  {converted_count}\nConvert successful.".format(
        preset_count=len(preset_xml_collection.keys()), converted_count=converted_count))


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.format_help()
    parser.add_argument("rpl_file", type=str, help="Input REAPER RPL file")
    parser.add_argument("target_path", type=str,
                        help="Where to put convert presets")
    parser.add_argument("-f", "--overwrite",
                        help="Remove all files in target path first (usually for distribution)", action="store_true")
    parser.add_argument("-t", "--type", type=str, default='auto', choices=('auto', 'synthv1', 'padthv1'),
                        help="Specify which Vee-One product you want to convert for. Case sensitive.\nChoices are: auto, synthv1, padthv1\nLeave blank for auto detection")
    args = parser.parse_args()

    rpl_to_xml(type=args.type, rpl_filename=args.rpl_file,
               target_path=args.target_path, overwrite_all=args.overwrite)


if __name__ == "__main__":
    main()
