class EditingDistances:

    def lcs(self, source, target, source_len, target_len, result):
        if source_len == 0 or target_len == 0:
            return result

        if source[source_len - 1] == target[target_len - 1]:
            result = self.lcs(source, target, source_len - 1, target_len - 1, result + 1)

        result = max(result, max(self.lcs(source, target, source_len, target_len - 1, 0),
                                 self.lcs(source, target, source_len - 1, target_len, 0)))

        return result

    def lcs_w_breaks(self, source, target, source_len, target_len):
        if source_len == 0 or target_len == 0:
            return 0

        elif source[source_len - 1] == target[target_len - 1]:
            return 1 + self.lcs_w_breaks(source, target, source_len - 1, target_len - 1)

        else:
            return max(self.lcs_w_breaks(source, target, source_len, target_len - 1),
                       self.lcs_w_breaks(source, target, source_len - 1, target_len))


def _print() -> None:
    #  Zad 3.a
    source1 = "kolorowy"
    target1 = "koralowy"
    sourceLen1 = len(source1)
    targetLen1 = len(target1)

    # Zad 3.b
    source2 = "kolorowy"
    target2 = "koralowy"
    sourceLen2 = len(source2)
    targetLen2 = len(target2)

    ##
    ed = EditingDistances()
    print(f"długość podciągu bez przerw wyraz {source1}, {target1}:")
    print(ed.lcs(source1, target1, sourceLen1, targetLen1, 0))
    print(f"dłguość podciągu z przerwami wyrazy {source2}, {target2}:")
    print(ed.lcs_w_breaks(source2, target2, sourceLen2, targetLen2))


_print()
