"""This module will be used for plotting radar chart & sub-plotting"""

from cosolidated_data import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

my_data = data_for_graph()
first_ps = list(my_data.keys())[0]
topper = top_performer()
bottom = bottom_performer()


def student_radar_graph(ps_no):
    """Function for generating a radar graph for students"""
    new_list = my_data[ps_no]
    for i in range(0, 4):
        if(i == 0):

            presurveylist = new_list[i]
            presurveyscore = presurveylist[0]
            presurveyavg = presurveylist[1]
            presurveymax = presurveylist[2]
            presurveymin = presurveylist[3]
            categories = ['Functions', 'Abstraction', 'Encapsulation',
                          'Inheritance', 'Polymorphism', "Unit-Testing", ""]

            presurveyscore = np.concatenate(
                (presurveyscore, [presurveyscore[0]]))
            presurveyavg = np.concatenate((presurveyavg, [presurveyavg[0]]))
            presurveymax = np.concatenate((presurveymax, [presurveymax[0]]))
            presurveymin = np.concatenate((presurveymin, [presurveymin[0]]))

            label_placement = np.linspace(
                start=0, stop=2*np.pi, num=len(presurveyscore))

            plt.figure(figsize=(6, 6))
            plt.subplot(polar=True)

            plt.plot(label_placement, presurveyscore)
            plt.plot(label_placement, presurveyavg)
            plt.plot(label_placement, presurveymax)
            plt.plot(label_placement, presurveymin)

            lines, labels = plt.thetagrids(
                np.degrees(label_placement), labels=categories)
            plt.title(f'PS Number :  {ps_no} - Pre Survey',
                      y=1.1, fontdict={'fontsize': 14})
            plt.legend(labels=['Score', 'Average',
                               'highest', 'Lowest'], loc=(0.95, 0.8))
            print(plt)
            plt.savefig(f'Presurvey_{ps_no}.png')
            img1 = Image.open(f'Presurvey_{ps_no}.png')

        if(i == 1):

            pretestlist = new_list[i]
            pretestscore = pretestlist[0]
            pretestavg = pretestlist[1]
            pretestmax = pretestlist[2]
            pretestmin = pretestlist[3]
            categories = ['Functions', 'Abstraction', 'Encapsulation',
                          'Inheritance', 'Polymorphism', "Unit-Testing", ""]

            pretestscore = np.concatenate((pretestscore, [pretestscore[0]]))

            pretestmax = np.concatenate((pretestmax, [pretestmax[0]]))
            pretestmin = np.concatenate((pretestmin, [pretestmin[0]]))
            pretestavg = np.concatenate((pretestavg, [pretestavg[0]]))

            label_placement = np.linspace(
                start=0, stop=2*np.pi, num=len(pretestscore))

            plt.figure(figsize=(6, 6))
            plt.subplot(polar=True)

            plt.plot(label_placement, pretestscore)

            plt.plot(label_placement, pretestmax)
            plt.plot(label_placement, pretestmin)
            plt.plot(label_placement, pretestavg)

            lines, labels = plt.thetagrids(
                np.degrees(label_placement), labels=categories)
            plt.title(f'PS Number :  {ps_no} - Pre Assessment',
                      y=1.1, fontdict={'fontsize': 14})
            plt.legend(labels=['Score', 'Average',
                               'highest', 'Lowest'], loc=(0.95, 0.8))

            plt.savefig(f'Pretest_{ps_no}.png')
            img2 = Image.open(f'Pretest_{ps_no}.png')

        if(i == 2):
            postsurveylist = new_list[i]
            postsurveyscore = postsurveylist[0]
            postsurveyavg = postsurveylist[1]
            postsurveymax = postsurveylist[2]
            postsurveymin = postsurveylist[3]
            categories = ['Functions', 'Abstraction', 'Encapsulation',
                          'Inheritance', 'Polymorphism', "Unit-Testing", ""]

            postsurveyscore = np.concatenate(
                (postsurveyscore, [postsurveyscore[0]]))
            postsurveyavg = np.concatenate((postsurveyavg, [postsurveyavg[0]]))
            postsurveymax = np.concatenate((postsurveymax, [postsurveymax[0]]))
            postsurveymin = np.concatenate((postsurveymin, [postsurveymin[0]]))

            label_placement = np.linspace(
                start=0, stop=2*np.pi, num=len(postsurveyscore))

            plt.figure(figsize=(6, 6))
            plt.subplot(polar=True)

            plt.plot(label_placement, postsurveyscore)
            plt.plot(label_placement, postsurveyavg)
            plt.plot(label_placement, postsurveymax)
            plt.plot(label_placement, postsurveymin)

            lines, labels = plt.thetagrids(
                np.degrees(label_placement), labels=categories)
            plt.title(f'PS Number :  {ps_no} - Post Survey',
                      y=1.1, fontdict={'fontsize': 14})
            plt.legend(labels=['Score', 'Average',
                               'highest', 'Lowest'], loc=(0.95, 0.8))

            plt.savefig(f'Postsurvey_{ps_no}.png')
            img3 = Image.open(f'Postsurvey_{ps_no}.png')

        if(i == 3):
            posttestlist = new_list[i]
            posttestscore = posttestlist[0]
            posttestavg = posttestlist[1]
            posttestmax = posttestlist[2]
            posttestmin = posttestlist[3]
            categories = ['Functions', 'Abstraction', 'Encapsulation',
                          'Inheritance', 'Polymorphism', "Unit-Testing", ""]

            posttestscore = np.concatenate((posttestscore, [posttestscore[0]]))
            posttestavg = np.concatenate((posttestavg, [posttestavg[0]]))
            posttestmax = np.concatenate((posttestmax, [posttestmax[0]]))
            posttestmin = np.concatenate((posttestmin, [posttestmin[0]]))

            label_placement = np.linspace(
                start=0, stop=2*np.pi, num=len(posttestscore))

            plt.figure(figsize=(6, 6))
            plt.subplot(polar=True)

            plt.plot(label_placement, posttestscore)
            plt.plot(label_placement, posttestavg)
            plt.plot(label_placement, posttestmax)
            plt.plot(label_placement, posttestmin)

            lines, labels = plt.thetagrids(
                np.degrees(label_placement), labels=categories)
            plt.title(f'PS Number :  {ps_no} - Post Assessment',
                      y=1.1, fontdict={'fontsize': 14})
            plt.legend(labels=['Score', 'Average',
                               'highest', 'Lowest'], loc=(0.95, 0.8))

            plt.savefig(f'Posttest_{ps_no}.png')
            img4 = Image.open(f'Posttest_{ps_no}.png')
    f, axarr = plt.subplots(2, 2)
    axarr[0, 0].imshow(img1)
    axarr[0, 1].imshow(img2)
    axarr[1, 0].imshow(img3)
    axarr[1, 1].imshow(img4)
    plt.savefig(f'Consolidated_{ps_no}.png', dpi=1000)


def faculty_radar_graph():
    """Function for generating a radar graph to faculties"""
    new_list = my_data[first_ps]
    for i in range(0, 4):
        if(i == 0):

            presurveylist = new_list[i]
            presurveyavg = presurveylist[1]
            presurveytopper = topper[i]

            presurveybottom = bottom[i]

            categories = ['Functions', 'Abstraction', 'Encapsulation',
                          'Inheritance', 'Polymorphism', "Unit-Testing", ""]

            presurveyavg = np.concatenate((presurveyavg, [presurveyavg[0]]))
            presurveytopper = np.concatenate(
                (presurveytopper, [presurveytopper[0]]))
            presurveybottom = np.concatenate(
                (presurveybottom, [presurveybottom[0]]))

            label_placement = np.linspace(
                start=0, stop=2*np.pi, num=len(presurveyavg))

            plt.figure(figsize=(6, 6))
            plt.subplot(polar=True)

            plt.plot(label_placement, presurveyavg)
            plt.plot(label_placement, presurveytopper)
            plt.plot(label_placement, presurveybottom)

            lines, labels = plt.thetagrids(
                np.degrees(label_placement), labels=categories)
            plt.title('Pre Survey Performance',
                      y=1.1, fontdict={'fontsize': 14})
            plt.legend(labels=['Average',
                               'Topper', 'Bottom'], loc=(0.95, 0.8))
            print(plt)
            plt.savefig(f'Presurvey_Performance.png')
            img1 = Image.open('Presurvey_Performance.png')

        if(i == 1):

            pretestlist = new_list[i]
            pretestavg = pretestlist[1]
            pretesttopper = topper[i]
            pretestbottom = bottom[i]

            categories = ['Functions', 'Abstraction', 'Encapsulation',
                          'Inheritance', 'Polymorphism', "Unit-Testing", ""]

            pretestavg = np.concatenate((pretestavg, [pretestavg[0]]))
            pretesttopper = np.concatenate((pretesttopper, [pretesttopper[0]]))
            pretestbottom = np.concatenate((pretestbottom, [pretestbottom[0]]))

            label_placement = np.linspace(
                start=0, stop=2*np.pi, num=len(pretestavg))

            plt.figure(figsize=(6, 6))
            plt.subplot(polar=True)

            plt.plot(label_placement, pretestavg)
            plt.plot(label_placement, pretesttopper)
            plt.plot(label_placement, pretestbottom)

            lines, labels = plt.thetagrids(
                np.degrees(label_placement), labels=categories)
            plt.title('Pre test Performance',
                      y=1.1, fontdict={'fontsize': 14})
            plt.legend(labels=['Average',
                               'Topper', 'Bottom'], loc=(0.95, 0.8))
            print(plt)
            plt.savefig(f'Pretest_Performance.png')
            img2 = Image.open('Pretest_Performance.png')
        if(i == 2):

            postsurveylist = new_list[i]
            postsurveyavg = postsurveylist[1]
            postsurveytopper = topper[i]
            postsurveybottom = bottom[i]

            categories = ['Functions', 'Abstraction', 'Encapsulation',
                          'Inheritance', 'Polymorphism', "Unit-Testing", ""]

            postsurveyavg = np.concatenate((postsurveyavg, [postsurveyavg[0]]))
            postsurveytopper = np.concatenate(
                (postsurveytopper, [postsurveytopper[0]]))
            postsurveybottom = np.concatenate(
                (postsurveybottom, [postsurveybottom[0]]))

            label_placement = np.linspace(
                start=0, stop=2*np.pi, num=len(postsurveyavg))

            plt.figure(figsize=(6, 6))
            plt.subplot(polar=True)

            plt.plot(label_placement, postsurveyavg)
            plt.plot(label_placement, postsurveytopper)
            plt.plot(label_placement, postsurveybottom)

            lines, labels = plt.thetagrids(
                np.degrees(label_placement), labels=categories)
            plt.title('Post Survey Performance',
                      y=1.1, fontdict={'fontsize': 14})
            plt.legend(labels=['Average',
                               'Topper', 'Bottom'], loc=(0.95, 0.8))
            print(plt)
            plt.savefig(f'Postsurvey_Performance.png')
            img3 = Image.open('Postsurvey_Performance.png')

        if(i == 3):

            posttestlist = new_list[i]
            posttestavg = posttestlist[1]
            posttesttopper = topper[i]
            posttestbottom = bottom[i]

            categories = ['Functions', 'Abstraction', 'Encapsulation',
                          'Inheritance', 'Polymorphism', "Unit-Testing", ""]

            posttestavg = np.concatenate((posttestavg, [posttestavg[0]]))
            posttesttopper = np.concatenate(
                (posttesttopper, [posttesttopper[0]]))
            posttestbottom = np.concatenate(
                (posttestbottom, [posttestbottom[0]]))

            label_placement = np.linspace(
                start=0, stop=2*np.pi, num=len(posttestavg))

            plt.figure(figsize=(6, 6))
            plt.subplot(polar=True)

            plt.plot(label_placement, posttestavg)
            plt.plot(label_placement, posttesttopper)
            plt.plot(label_placement, posttestbottom)

            lines, labels = plt.thetagrids(
                np.degrees(label_placement), labels=categories)
            plt.title('Post test Performance',
                      y=1.1, fontdict={'fontsize': 14})
            plt.legend(labels=['Average',
                               'Topper', 'Bottom'], loc=(0.95, 0.8))
            print(plt)
            plt.savefig(f'Posttest_Performance.png')
            img4 = Image.open('Posttest_Performance.png')

    f, axarr = plt.subplots(2, 2)
    axarr[0, 0].imshow(img1)
    axarr[0, 1].imshow(img2)
    axarr[1, 0].imshow(img3)
    axarr[1, 1].imshow(img4)
    plt.savefig('Consolidated_class.png', dpi=1000)
