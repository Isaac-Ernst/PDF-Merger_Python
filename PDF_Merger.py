#
# PDF Merger-V1 (5/11-12/2023)
# Isaac B. Ernst
#

from pypdf import PdfMerger

merger = PdfMerger()

responses = ['yes', 'y', 'yep']

pdfs = {}

# Checks pdf names...
def checkpdf(ans):
    correct = input("Correct? ")
    if correct not in ans:
        return None
    else:
        return 1


# Gets pages for each pdf...
def getpages(pdf, ans):
    while True:
        try:
            pages = input(f"Enter pages for {pdf} (ex: 1, 2, 3...) (a to merge entire file): ")
            if pages not in 'a':
                pages = [int(i) for i in pages.split(',')]
            if checkpdf(ans) == None:
                continue
            break

        except:
            print("Bad input.")
    return pages


# Gets pdf names...
def getpdf(resp):
    while True:
        pdf_name = input("Enter file (q to quit; c to continue): ")
        if pdf_name == 'q':
            return pdf_name
        elif pdf_name == 'c':
            break
        else:
            if checkpdf(resp) == None:
                continue
            pdfs[pdf_name] = getpages(pdf_name, resp)


# Gets number of page values...
def getnumvals(pdfs):
    list_vals = [vals for vals in pdfs.values()]
    i = 0
    for list_val in list_vals:
        for vals in list_val:
            i += 1
    return i


# Reduces inefficient code re-use...
def stopper_checker(resp, pdfs_list, num):
    if checkpdf(resp) == None:
        return False
    if num == getnumvals(pdfs_list):
        return True

# Get order of appending...
def getorder(resp, pdfs_list):
    print("Getting order of pages and files...")
    order = []
    i = 0
    while True:
        try:
            file = input("Enter file (q to quit; m to merge): ")
            i += 1
            if file == 'q':
                i -= 1
                break
            elif file == 'm':
                break
            if file not in pdfs_list.keys():
                raise TypeError
            if pdfs_list[file] == 'a':
                i += 1
                if stopper_checker(resp, pdfs_list, i) == False:
                    i -= 1
                    continue
                else:
                    order.append([file, pdfs_list[file]])
                    break
            else:
                page = input("Enter page number: ")
                if int(page) not in pdfs_list[file]:
                    i -= 1
                    raise TypeError
                if [file, int(page)] in order:
                    raise TypeError
                if stopper_checker(resp, pdfs_list, i) == False:
                    i -= 1
                    continue
                else:
                    order.append([file, int(page)])
                    break

        except:
            print('Bad input.')
    return order


# Mergers pdfs in order of file and page...
def merge_pdfs(order):
    for vals in order:
        print(vals)
        if vals[-1] == 'a':
            merger.append(vals[0] + '.pdf')
        else:
            merger.append(vals[0] + '.pdf', pages=(vals[-1] - 1, vals[-1]))
    merger.write("merged_file.pdf")
    merger.close()


# Main function...
def main(resp, pdf_list):
    if getpdf(resp) == 'q':
        pass
    elif {} != pdf_list:
        print(pdf_list)
        merge_pdfs(getorder(resp, pdf_list))


main(responses, pdfs)
