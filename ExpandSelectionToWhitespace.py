import sublime
import sublime_plugin
import re


class ExpandSelectionToWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selected_regions = self.view.sel()
        for region in selected_regions:
            expanded_region = self.expand_region_to_whitespace(region)
            if expanded_region:
                selected_regions.add(expanded_region)

    def expand_region_to_whitespace(self, region):
        # consider only the lines containing the region
        whole_lines_region = self.view.line(region)
        if not whole_lines_region:
            return None
        whole_lines_string = self.view.substr(whole_lines_region)

        # look for a whitespace boundary at the beginning of the region,
        # or between the beginning of the region and the beginning of the line it starts on
        region_begin_within_whole_lines = region.begin() - whole_lines_region.begin()
        whitespace_boundary_begin_within = self.find_whitespace_boundary_at_or_before(whole_lines_string, region_begin_within_whole_lines)

        # look for whitespace between end of the region and the end of the line it ends on
        region_end_within_whole_lines = region.end() - whole_lines_region.begin()
        whitespace_boundary_end_within = self.find_whitespace_boundary_at_or_after(whole_lines_string, region_end_within_whole_lines)

        # return region expanded to whitespace boundaries
        expanded_region_begin = whole_lines_region.begin() + whitespace_boundary_begin_within
        expanded_region_end = whole_lines_region.begin() + whitespace_boundary_end_within
        return sublime.Region(expanded_region_begin, expanded_region_end)

    # position of the closest whitespace boundary between pos and the beginning of the string
    # or the beginning of the string if there are none
    def find_whitespace_boundary_at_or_before(self, str, pos):
        # \S matches any character not marked as space in the Unicode character properties database
        match = re.search(r"\S+$", str[:pos], re.UNICODE)
        if match:
            return pos - (match.end() - match.start())
        # when not preceded by whitespace, set pos as the boundary
        return pos

    # position of the closest whitespace boundary between pos and the end of the string,
    # or the end of the string if there are none
    def find_whitespace_boundary_at_or_after(self, str, pos):
        # \s matches [ \t\n\r\f\v] plus whatever is classified as space in the Unicode character properties database
        match = re.search(r"\s", str[pos:], re.UNICODE)
        if match:
            return pos + match.start()
        return len(str)
